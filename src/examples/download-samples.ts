import { type AudiotoolClient } from "audiotool-nexus";

/**
 * Download samples from a project
 * @param audiotool - The audiotool client
 * @param project - The project URL
 * @param sampleType - The type of samples to download (mp3, flac, wav)
 * @throws {Error} If sample info cannot be fetched
 */
export const downloadSamples = async (
  audiotool: AudiotoolClient,
  project: string,
  sampleType: "mp3" | "flac" | "wav" = "mp3"
) => {
  // STEP 1: connect to the given project
  const nexus = await audiotool.createSyncedDocument({
    mode: "online",
    project,
  });

  await nexus.start();

  // STEP 2: get the list of all audio regions
  const audioRegions = nexus.queryEntities.ofTypes("audioRegion").get();

  if (audioRegions.length === 0) {
    throw new Error("No audio regions found in the project");
  }

  const downloadedSamples = [];

  // STEP 3: process each audio region to download its sample
  for (const region of audioRegions) {
    // get the sample entity that the region points to
    const sampleEntity = nexus.queryEntities.mustGetEntityAs(
      region.fields.sample.value.entityId,
      "sample"
    );

    // this is the sample "name", the identifier used in the backend
    const sampleName = sampleEntity.fields.sampleId.value;

    // get more info on the sample using the API
    const sampleInfo = await audiotool.api.sampleService.getSample({
      name: sampleName,
    });
    if (sampleInfo instanceof Error) {
      throw new Error("Couldn't fetch sample info for audio region", {
        cause: sampleInfo,
      });
    }

    // determine the URL based on sample type
    let sampleUrl: string | undefined;
    switch (sampleType.toLowerCase()) {
      case "flac":
        sampleUrl = sampleInfo.sample?.flacUrl;
        break;
      case "wav":
        sampleUrl = sampleInfo.sample?.wavUrl;
        break;
      default:
      case "mp3":
        sampleUrl = sampleInfo.sample?.mp3Url;
        break;
    }

    if (!sampleUrl) {
      throw new Error(
        `No ${sampleType} URL available for sample ${sampleName}`
      );
    }

    // download the sample data
    const response = await fetch(sampleUrl);
    const sampleData = await response.arrayBuffer();

    // create a blob and object URL for the downloaded sample
    const mimeType = `audio/${sampleType.toLowerCase()}`;
    const blob = new Blob([sampleData], { type: mimeType });
    const url = URL.createObjectURL(blob);

    downloadedSamples.push({
      name: region.fields.region.fields.displayName.value,
      sampleName,
      url,
      blob,
      data: sampleData,
      type: sampleType.toLowerCase(),
    });
  }

  return downloadedSamples;
};

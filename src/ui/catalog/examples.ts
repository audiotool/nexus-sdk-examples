import type { AudiotoolClient } from "audiotool-nexus";
import { createSound } from "../../examples/create-sound";
import { downloadSamples } from "../../examples/download-samples";
import { createProject } from "../../examples/create-project";

export type Example = {
  title: string;
  description: string;
  requirements: string[];
  actionLabel: string;
  action: (audiotool: AudiotoolClient, ...args: string[]) => Promise<void>;
};

export const EXAMPLE_CREATE_SOUND: Example = {
  title: "Create Sound",
  description: "Create a sound with a tonematrix in the specified project",
  requirements: ["Project URL"],
  actionLabel: "Create Sound",
  action: async (audiotool, projectURL) => {
    console.clear();
    console.log("Creating sound...");

    // create sound
    await createSound(audiotool, projectURL);

    console.log(
      "A new tonematrix has been created in the project and connected to a free mixer channel."
    );
    console.log(
      "This has been configured to use a randomly generated pattern."
    );
    console.log(`Visit the project to hear the sound: ${projectURL}`);
  },
};

export const EXAMPLE_DOWNLOAD_SAMPLES: Example = {
  title: "Download Samples",
  description: "Download samples from a project",
  requirements: ["Project URL", "Sample Type (optional, defaults to mp3)"],
  actionLabel: "Download Samples",
  action: async (audiotool, projectURL, sampleType = "mp3") => {
    console.clear();

    if (!["mp3", "flac", "wav"].includes(sampleType)) {
      console.log(
        `Invalid sample type: ${sampleType}. Please choose from mp3, flac, or wav.`
      );
      return;
    }

    console.log("Downloading samples...");

    try {
      // download samples
      const samples = await downloadSamples(
        audiotool,
        projectURL,
        sampleType as "mp3" | "flac" | "wav"
      );

      console.log(
        `Successfully downloaded ${
          samples.length
        } samples as ${sampleType.toUpperCase()}`
      );

      // log details about each downloaded sample
      samples.forEach((sample, index) => {
        console.log(`${index + 1}. ${sample.name} (${sample.sampleName})`);
      });

      console.log(`\nAll samples are now available as blobs in memory.`);
      console.log(`You can access them programmatically or save them to disk.`);
      console.log(`\nProject: ${projectURL}`);
    } catch (error) {
      console.log(
        `Error: Failed to download samples: ${
          error instanceof Error ? error.message : String(error)
        }`
      );
      if (error instanceof Error && error.cause) {
        console.log(`Error cause: ${error.cause}`);
      }
    }
  },
};

export const EXAMPLE_SET_PAT: Example = {
  title: "Set Personal Access Token",
  description: "Set or update your personal access token",
  requirements: ["Personal Access Token"],
  actionLabel: "Set Token",
  action: async (audiotool, pat) => {
    // TODO: implement actual PAT setting logic
  },
};

export const EXAMPLE_CREATE_PROJECT: Example = {
  title: "Create Project",
  description: "Create a new project using the project service",
  requirements: ["Project Display Name"],
  actionLabel: "Create Project",
  action: async (audiotool, displayName) => {
    console.clear();
    console.log("Creating new project...");

    try {
      // create project
      const projectInfo = await createProject(audiotool, displayName);

      console.log("Project created successfully!");
      console.log(`Project Name: ${projectInfo.displayName}`);
      console.log(`Backend Name: ${projectInfo.name}`);
      console.log(`Creator: ${projectInfo.creatorName}`);
      console.log(`Project URL: ${projectInfo.url}`);
    } catch (error) {
      console.log(
        `Error: Failed to create project: ${
          error instanceof Error ? error.message : String(error)
        }`
      );
    }
  },
};

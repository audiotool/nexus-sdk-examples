import { setupAudiotoolDocument } from "@audiotool/nexus"
import { throw_ } from "@audiotool/nexus/utils"

// This example assumes you're connecting to an audiotool project which has some
// sample regions in it.

const {nexus, api} = await setupAudiotoolDocument({
    mode: "online",
    project: "https://beta.audiotool.com/studio?project=0410b64e-ba1c-477e-a995-7e2bc1697576"
})

const t = await nexus.createTransaction()
const regions = t.entities.ofTypes("audioRegion").get()

for (const region of regions){
    console.debug("got sample region with name ", region.fields.region.fields.displayName.value, "on track connected to  name", t.entities.ofTypes("desktopPlacement").pointingTo.entities(region.fields.track.value.entityId).get()[0].fields.displayName.value)
    const sampleEntity = t.entities.mustGetEntityAs(region.fields.sample.value.entityId, "sample")
    const sampleName = sampleEntity.fields.sampleId.value
    console.debug("getting info for sample with name", sampleName)
    const sampleInfo = await api.sampleService.getSample({name: sampleName})
    if (sampleInfo instanceof Error){
        throw new Error("couldn't fetch sample info for audio region", {cause: sampleInfo})
    }
    console.debug("got urls:", {
        flac: sampleInfo.sample?.flacUrl,
        mp3: sampleInfo.sample?.mp3Url,
        wav: sampleInfo.sample?.wavUrl
    })

    const flacData = await fetch(sampleInfo.sample?.flacUrl ?? throw_()).then(res => res.arrayBuffer())

    // now we've got the flac data, to do as we like. In the remainder of this function,
    // we decode the audio, and play is using an audio context, before continuing with
    // the next region.

    const ctx = new AudioContext()
    console.debug("decoding audio data...")
    const audioBuffer = await ctx.decodeAudioData(flacData)
    console.debug("Done!")

    
    const node = ctx.createBufferSource()
    node.buffer = audioBuffer
    node.connect(ctx.destination)

    // promise resolves when playback ends
    const stopPromise = new Promise<void>(res => node.onended = (() => res()))
    node.start()
    
    console.debug("playing buffer...")
    await stopPromise
}
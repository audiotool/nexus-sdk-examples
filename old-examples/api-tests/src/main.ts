import { createAudiotoolClient } from "@audiotool/nexus"

const client = await createAudiotoolClient()

const apiTestsForm = document.getElementById(
  "api-tests-form"
) as HTMLFormElement
const patInput = document.getElementById("pat") as HTMLInputElement

apiTestsForm.addEventListener("submit", async (e) => {
  e.preventDefault()

  // set PAT
  client.setPAT(patInput.value)
})

const nexusDocument = await client.createSyncedDocument({
  mode: "offline",
  validated: false,
})
await nexusDocument.start()

/** sample service examples */
const samples = async () => {
  const sampleEntity = nexusDocument.queryEntities.ofTypes("sample").getOne()
  if (sampleEntity === undefined) {
    console.warn("no sample entity")
    return
  }

  const sample = await client.api.sampleService.getSample({
    name: sampleEntity.fields.sampleId.value,
  })

  if (sample instanceof Error) {
    throw sample
  }

  console.log("wav url", sample.sample?.wavUrl)
}

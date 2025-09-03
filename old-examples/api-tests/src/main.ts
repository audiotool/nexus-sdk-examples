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

/** user service examples */
const userService = async () => {
  const current = await client.api.userService.getUser({})
  if (current instanceof Error) {
    throw current
  }
  console.debug(
    "Current user:",
    current.user?.name,
    "display name:",
    current.user?.displayName
  )

  const otherUser = await client.api.userService.getUser({
    name: "users/kepz",
  })
  if (otherUser instanceof Error) {
    throw otherUser
  }
  console.debug("kepz is", otherUser.user?.displayName)

  // const search = await client.api.userService.listUsers({
  //   filter: "user.display_name='SilasGyger'",
  // })
  // if (search instanceof Error) {
  //   throw search
  // }
  // console.table(
  //   search.users.map((u) => ({
  //     name: u.name,
  //     displayName: u.displayName,
  //   }))
  // )
}

// await userService()

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

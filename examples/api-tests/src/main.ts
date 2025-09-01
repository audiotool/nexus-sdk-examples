import { createAudiotoolClient } from "@audiotool/nexus"

const client = await createAudiotoolClient()

// get the pat token.
fetch("./pat")
  .then(async (res) => client.setPAT(await res.text()))
  .catch(() => {
    console.warn("couldn't fetch pat, create ../../pat.txt")
  })

//** project service examples */
const projectService = async () => {
  const projects = await client.api.projectService.listProjects({})
  if (projects instanceof Error) {
    console.error(projects)
  } else {
    console.table(
      projects.projects.map((p) => ({
        name: p.displayName,
        backendName: p.name,
        creator: p.creatorName,
      }))
    )
  }

  // turned off to avoid noise
  if (false) {
    await client.api.projectService.createProject({
      project: {
        displayName: "My New Project",
      },
    })
  }
}

// await projectService()

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

const document = await client.createSyncedDocument({
  mode: "offline",
  validated: false,
})
await document.start()

/** sample service examples */
const samples = async () => {
  const sampleEntity = document.queryEntities.ofTypes("sample").getOne()
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

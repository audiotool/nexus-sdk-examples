import { setPAT, setupAudiotoolProject } from "@audiotool/nexus"

const throw_ = () => {
  throw new Error()
}

// get the pat token.
fetch("./pat")
  .then(async (res) => setPAT(await res.text()))
  .catch(() => {
    console.warn("couldn't fetch pat, create ../../pat.txt")
  })

// connect to some project.
const { nexus, api } = await setupAudiotoolProject({
  mode: "online",
  project:
    "https://beta.audiotool.com/studio?project=0410b64e-ba1c-477e-a995-7e2bc1697576",
})

await nexus.start()

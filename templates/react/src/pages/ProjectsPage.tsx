import { useProjects } from "@/hooks/useProjects"
import { AudiotoolClient } from "@audiotool/nexus"

interface ProjectsPageProps {
    client: AudiotoolClient
}
function ProjectsPage({ client }: ProjectsPageProps) {
    // Fetch projects using the authenticated client
    const projectsResult = useProjects(client)

    // Create a new project and open it in Audiotool Studio
    const handleNewProject = async () => {
        if (projectsResult.case !== 'loaded') return
        const created = await projectsResult.createProject('New Project')
        created?.name
        window.open(`https://beta.audiotool.com/studio?project=${created?.name}`, '_blank')
    }

    return (
        <>
        <div>
        Successfully Logged In! Welcome!
        </div>

        {/* Show loading state while fetching projects */}
        {projectsResult.case === 'loading' && (
            <div className="projects-loading">
                <p>Loading projects...</p>
            </div>
        )}
        {/* Show error state with retry option */}
        {projectsResult.case === 'error' && (
            <div className="projects-error">
              <p>Failed to load projects: {projectsResult.error}</p>
              <button onClick={projectsResult.retry} className="retry-btn">
                Retry
              </button>
            </div>
        )}
        {/* Show projects list when loaded */}
        {projectsResult.case === 'loaded' && (
            <div className="projects-loaded">
                <button onClick={() => {
                    handleNewProject()
                }}>Create New Project</button>
                <br />
                Existing Projects: 
                <select>
                    {projectsResult.projects.map((project) => {
                        return (
                            <option key={project.name} value={project.name}>{project.displayName}</option>
                        )
                    })}
                </select>
            </div>
        )}
        
        </>
  )
}

export default ProjectsPage
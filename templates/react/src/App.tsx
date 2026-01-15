import { useLoginStatus } from './hooks/useLoginStatus'
import { LoginPage } from './pages/LoginPage'
import ProjectsPage from './pages/ProjectsPage'

function App() {
  const loginStatus = useLoginStatus()

  // Loading state
  if (loginStatus.case === 'loading') {
    return (
      <LoginPage
        onLogin={() => {}}
        isLoading={true}
      />
    )
  }

  // Error state
  if (loginStatus.case === 'error') {
    return (
      <LoginPage
        onLogin={() => {}}
        error={loginStatus.error}
        onRetry={loginStatus.retry}
      />
    )
  }

  // Logged out - show login page
  if (loginStatus.case === 'loggedOut') {
    return (
      <LoginPage
        onLogin={loginStatus.login}
      />
    )
  }

  return (<ProjectsPage client={loginStatus.client} />)

}

export default App

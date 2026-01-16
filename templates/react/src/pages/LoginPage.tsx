interface LoginPageProps {
  onLogin: () => void
  isLoading?: boolean
  error?: string
  onRetry?: () => void
}

export function LoginPage({ onLogin, isLoading, error, onRetry }: LoginPageProps) {
  // Show loading spinner while checking login status
  if (isLoading) {
    return (
      <div className="login-page">
        <div className="login-card">
          <div className="login-loading">
            <div className="spinner"></div>
            <p>Connecting to Audiotool...</p>
          </div>
        </div>
      </div>
    )
  }

  // Show error message with retry option if login check failed
  if (error) {
    return (
      <div className="login-page">
        <div className="login-card login-card-error">
          <h1>Audiotool Vocoder</h1>
          <p className="login-error-message">{error}</p>
          {onRetry && (
            <button onClick={onRetry} className="login-btn">
              Try Again
            </button>
          )}
        </div>
      </div>
    )
  }

  // Show login button to initiate OAuth flow
  return (
    <div className="login-page">
      <div className="login-card">
        <h1>Audiotool React Template</h1>
        <p className="login-description">
          You need to authorize this application to continue.
        </p>
        <button onClick={onLogin} className="login-btn">
          Login with Audiotool
        </button>
      </div>
    </div>
  )
}

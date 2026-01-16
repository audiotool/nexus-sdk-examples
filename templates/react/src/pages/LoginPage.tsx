interface LoginPageProps {
  onLogin: () => void
  isLoading?: boolean
  error?: string
  onRetry?: () => void
}

export function LoginPage({ onLogin, isLoading, error, onRetry }: LoginPageProps) {
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

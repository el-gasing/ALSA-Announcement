import React from "react";
import goldLogo from "../PAMFLET GD BARU_20260422_154313_0000.png";
import unhasLogo from "../Logo-Resmi-Unhas-1-768x918.png";
import alsaLogo from "../logo alsa putih.png";

function BrandLogos() {
  return (
    <header className="brand-row" aria-label="Logo organisasi">
      <img
        className="logo-unhas"
        src={unhasLogo}
        alt="Logo Universitas Hasanuddin"
      />
      <img className="logo-alsa" src={alsaLogo} alt="Logo ALSA" />
      <img className="logo-gold" src={goldLogo} alt="Logo emas" />
    </header>
  );
}

function FieldIcon({ type }) {
  if (type === "lock") {
    return (
      <span className="lock-icon">
        <span className="lock-dot" />
      </span>
    );
  }

  return <span className="person-icon" />;
}

function LoginField({ id, label, type = "person", inputMode, autoComplete }) {
  return (
    <div className="field">
      <label htmlFor={id}>{label}</label>
      <div className="input-shell">
        <div className="icon-box" aria-hidden="true">
          <FieldIcon type={type} />
        </div>
        <input
          id={id}
          name={id}
          inputMode={inputMode}
          autoComplete={autoComplete}
        />
      </div>
    </div>
  );
}

function App() {
  return (
    <div className="mobile-frame">
      <BrandLogos />

      <main>
        <h1>
          Department
          <br />
          Announcement
        </h1>

        <form className="login-panel" action="#" method="post">
          <LoginField id="nama" label="Nama" autoComplete="name" />
          <LoginField
            id="nim"
            label="NIM"
            type="lock"
            inputMode="numeric"
            autoComplete="off"
          />
        </form>

        <button className="login-button" type="button">
          LOGIN
        </button>

        <p className="tagline">
          <span>ALSA,</span>
          <span>Always be One!</span>
        </p>
      </main>
    </div>
  );
}

export default App;

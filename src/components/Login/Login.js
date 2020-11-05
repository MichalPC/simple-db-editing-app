import './Login.css';
import { Link, useHistory } from 'react-router-dom'
import React, { useState } from 'react';

function Login() {
  const [curUsername, setCurUsername] = useState('')
  const [curPassword, setCurPassword] = useState('')
  const history = useHistory();

  const setUsername= (e) => {
    setCurUsername(e.target.value)
  }

  const setPassword= (e) => {
    setCurPassword(e.target.value)
  }

  const checkLogin = (e) => {
    if (curUsername === 'logged' && curPassword === 'in') {
      history.push('/home')
    } else {
      console.log('try again')
    }
  }

  return (
    <div className="Login">
      <main className="Login-container">
        <form className="Login-form">
          <input type="text" value={curUsername} onChange={setUsername}></input>
          <input className="Password-input"type="text" value={curPassword} onChange={setPassword}></input>
          <button type='button' onClick={checkLogin} >Login</button>
        </form>
        <Link className='Login-button' to={'/home'}> Login </Link>
      </main>
    </div>
  );
}

export default Login;

import axios from 'axios';
import { useGoogleLogin } from '@react-oauth/google';
import {} from 'react-router-dom';

export default function Login() {
  const scope = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/calendar.app.created",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid"
  ];

  console.log('escopo configurado:');
  console.log(scope);

  const handleLogin = async (credentialResponse) => {
    console.log('credential Response', credentialResponse);

    try {
      const response = await axios.post('http://localhost:8000/api/v1/calendar/token/', credentialResponse, {
        headers: {
          'Content-Type': 'application/json',
        }
      });

      console.log('response-data: ', response.data);
    } catch (error) {
      console.error('error: ', error);
    }
  }

  const login = useGoogleLogin({
    scope: "https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.app.created https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile openid",
    flow: 'auth-code',
    access_type: 'offline',
    prompt: 'consent',
    onSuccess: handleLogin,
  });

  return (<button onClick={() => login()}> Fazer login</button>);
}

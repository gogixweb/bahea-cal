import  { useEffect } from 'react';
import axios from 'axios';
import { useGoogleLogin } from '@react-oauth/google';
import {} from 'react-router-dom';
import { useNavigate } from 'react-router-dom';



export default function Login() {

  const navigate = useNavigate();

  const scope = [
    "https://www.googleapis.com/auth/calendar.app.created",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/calendar",
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

      console.log('token-data: ', response.data.token);
      localStorage.setItem('accessToken', response.data.token);
     
    } catch (error) {
      console.error('error: ', error);
    }
  }

  const login = useGoogleLogin({
    scope: "https://www.googleapis.com/auth/calendar.app.created https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/calendar openid",
    flow: 'auth-code',
    access_type: 'offline',
    prompt: 'consent',
    onSuccess: handleLogin,
  });


  useEffect(() => {
    const loginData = localStorage.getItem('accessToken');
    if (loginData) {
      navigate('../settings');
    }
  }, [navigate]);


  return (<button onClick={() => login()}> Fazer login</button>);
}

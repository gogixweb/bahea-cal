// import React from 'react';
import BahiaLogo from '../assets/bahia.png'; // Corrigindo o caminho para os arquivos de imagem
import flamengologo from '../assets/flamengo1.png';
import palmeiraslogo from '../assets/palmeiras.png';
import atleticologo from   '../assets/atletico.png';
import fluminenselogo from '../assets/fluminense.png';
import corinthiaslogo from '../assets/corinthias.png';
import { useGoogleLogin } from '@react-oauth/google';
import {} from 'react-router-dom';
import axios from 'axios';

export default function Club(){

  const scope = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/calendar.app.created",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid"
  ];

  console.log('escopo configurado:');
  console.log(scope);

  // Função para mostrar o escudo quando o botão é clicado
  // const showLogo = (teamName) => {
  //   alert(`Você selecionou o ${teamName}`);
  //   // Aqui você pode adicionar lógica para exibir o escudo
  // }

  const handleLogin = async (credentialResponse) => {
    const apiUrl = process.env.REACT_APP_API_URL + '/api/v1/calendar/token/';


    console.log('credential Response', credentialResponse);

    try {
        const response = await axios.post(apiUrl, credentialResponse, {
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


  return (
    <div className="container text-center mt-5">
    <h1>Adicione Jogos do Seu Time</h1>
    <h3>no calendário do seu celular</h3>
    
    <div className="my-4">
      <button onClick={login} className="btn btn-primary">
        <img src={BahiaLogo} alt="Bahia" className="img-fluid" style={{ width: '50px', height: '50px' }} /> Bahia
      </button>
    </div>
    
    <h5>Em breve...</h5>
    
    <div className="d-flex justify-content-center flex-wrap mt-3">
      <button className="btn btn-outline-secondary m-2">
        <img src={flamengologo} alt="Flamengo" className="img-fluid" style={{ width: '50px', height: '50px' }} /> Flamengo
      </button>
      <button className="btn btn-outline-secondary m-2">
        <img src={palmeiraslogo} alt="Palmeiras" className="img-fluid" style={{ width: '50px', height: '50px' }} /> Palmeiras
      </button>
      <button className="btn btn-outline-secondary m-2">
        <img src={corinthiaslogo} alt="Corinthians" className="img-fluid" style={{ width: '50px', height: '50px' }} /> Corinthians
      </button>
      <button className="btn btn-outline-secondary m-2">
        <img src={fluminenselogo} alt="Fluminense" className="img-fluid" style={{ width: '50px', height: '50px' }} /> Fluminense
      </button>
      <button className="btn btn-outline-secondary m-2">
        <img src={atleticologo} alt="Atlético" className="img-fluid" style={{ width: '50px', height: '50px' }} /> Atlético
      </button>
    </div>
  </div>
  
    );
}

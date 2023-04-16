import * as firebase from 'firebase/app'

const firebaseConfig = {
  apiKey: 'AIzaSyD68V0I2WhkaP3j49BuwBiEYqSJkePjTUk',
  authDomain: 'swarm-learning-ecg.firebaseapp.com',
  projectId: 'swarm-learning-ecg',
  storageBucket: 'swarm-learning-ecg.appspot.com',
  messagingSenderId: '1060718013443',
  appId: '1:1060718013443:web:5829cae0f6cc79c920b236',
  measurementId: 'G-D3NT7LC0D0',
}

let app = null
if (!firebase.app.length) {
  // Initialize Firebase
  app = initializeApp(firebaseConfig)
}

export default firebase

import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')

import axios from 'axios';

let url = "http://localhost:8000/user/";

axios.get(url)
.then(function(response){
    console.log(response);
}) //get request success
.catch(function(response){
    console.log(response);
}) //get resuest fail
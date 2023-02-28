import Vue from 'vue'
import {createApp} from 'vue'
import App from './App.vue'

createApp(App).mount('#app')

import axios from 'axios';

// 다른 컴포넌트에서 import 안하고 사용 가능 -> this.$axios
Vue.prototype.$eventBus = new Vue();
Vue.prototype.$axios = axios

let url = "http://localhost:8000/user/";

axios.get(url)
.then(function(response){
    console.log('success');
    console.log(response);
}) //get request success
.catch(function(response){
    console.log('fail');
    console.log(response);
}) //get resuest fail
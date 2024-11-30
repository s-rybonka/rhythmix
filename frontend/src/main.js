import Vue from 'vue'
import pinia from '@/store'
import router from '@/router'
import axios from 'axios'
import App from '@/App.vue'
import './registerServiceWorker'
import './plugins/bootstrap-vue'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'


Vue.config.productionTip = false


new Vue({
  el: '#app',
  render: (h) => h(App),
  router, pinia,
})

import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from './views/HomeView.vue'
import AboutView from './views/AboutView.vue'
import SongsView from './views/SongsView.vue'
import LoginView from "@/views/LoginView.vue";
import ProfileView from "@/views/ProfileView.vue";
import LogoutView from "@/views/LogoutView.vue";


const routes = [
  {path: '/', component: HomeView},
  {path: '/about', component: AboutView},
  {path: '/songs', component: SongsView},
  {path: '/login', component: LoginView},
  {path: '/logout', component: LogoutView},
  {path: '/profile', component: ProfileView}
]

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router

import Vue from 'vue'
import VueRouter from 'vue-router'
import ExampleComponent from "@/components/ExampleComponent.vue";

const routes = [
  {path: '/', component: ExampleComponent},
]

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router

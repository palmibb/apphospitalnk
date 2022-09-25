import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import LogIn from './components/LogIn.vue'
import Home from'./components/Inicio.vue'
import SignUp from'./components/Registrarse.vue'
const routes = [
  {
    path: '/',
    name: 'root',
    component: App
  },
  {
    path: '/usuario/inicio',
    name: 'home',
    component: Home
  },
  {
    path: '/usuario/ingreso',
    name: 'logIn',
    component: LogIn
  },
  {
    path: '/usuario/registrar',
    name: 'signUp',
    component: SignUp
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

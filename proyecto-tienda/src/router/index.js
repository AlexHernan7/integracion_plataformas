import { createRouter, createWebHashHistory } from 'vue-router'
import HomeTienda from '@/views/HomeTienda.vue';
import ProductosTienda from '@/views/ProductosTienda.vue';
import MensajeriaTienda from '@/views/MensajeriaTienda';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeTienda
  },
  {
    path: '/productos',
    name: 'ProductosTienda',
    component: ProductosTienda
  },
  {
    path: '/mensajeria',
    name: 'MensajeriaTienda',
    component: MensajeriaTienda
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

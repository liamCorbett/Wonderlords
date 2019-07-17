import Vue from 'vue';
import Router from 'vue-router';
import Builds from './components/Builds.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Builds',
      component: Builds,
    },
  ],
});

import Vue from 'vue';
import Router from 'vue-router';
import VTooltip from 'v-tooltip';

import Builds from './components/Builds.vue';

Vue.use(Router);
Vue.use(VTooltip, {
  defaultDelay: {
    show: 350,
  },
});

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

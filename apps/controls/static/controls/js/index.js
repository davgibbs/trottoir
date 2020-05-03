import '@babel/polyfill';
import Vue from 'vue';
// import VueRouter from 'vue-router';
// import Raven from 'raven-js';
import App from './App.vue';
/*
Raven
  .config('https://d7575428d2b54cc8ba053fd7aa506ad5@sentryv2.openapp.ie/11')
  .install();

Vue.use(VueRouter);

// This router is only defined to read the query params of a previous session
const router = new VueRouter({
  mode: 'hash',
  routes: [
    { path: '/:sessionid', name: 'session', component: App },
  ],
});
*/
// eslint-disable-next-line no-new
new Vue({
  // router,
  el: '#app',
  render: (h) => h(App),
});

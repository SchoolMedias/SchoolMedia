import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import video from '@/components/video'
import live from '@/components/live'
import meeting from '@/components/meeting'
import user from '@/components/user'
Vue.use(Router)
Vue.config.debug = true;
export default new Router({
  routes: [
    {
      path: '/123',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/321',
      name: 'Home',
      component: Home
    },
    {
      path: '/video',
      name: 'video',
      component: video
    },
    {
      path: '/meeting',
      name: 'meeting',
      component: meeting
    },
    {
      path: '/user',
      name: 'user',
      component: user
    },
    {
      path: '/live',
      name: 'live',
      component: live
    }
  ]
})


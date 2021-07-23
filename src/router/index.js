import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "home" */ '../views/home/home.vue')
  },
  {
    path: '/shop/:id',
    name: 'Shop',
    component: () => import(/* webpackChunkName: "shop" */ '../views/shop/Shop.vue')
  },
  {
    path: '/orderConfirm/:id',
    name: 'OrderConfirm',
    component: () => import(/* webpackChunkName: "orderConfirm" */ '../views/orderConfirmation/orderConfirm.vue')
  },
  {
    path: '/orderList',
    name: 'OrderList',
    component: () => import(/* webpackChunkName: "orderList" */ '../views/orderList/orderList.vue')
  },
  {
    path: '/cartList',
    name: 'CartList',
    component: () => import(/* webpackChunkName: "cartList" */ '../views/cartList/CartList.vue')
  },
  {
    path: '/user',
    name: 'User',
    component: () => import(/* webpackChunkName: "user" */ '../views/user/user.vue')
  },
  {
    path: '/Login',
    name: 'Login',
    component: () => import(/* webpackChunkName: "login" */ '../views/login/login.vue')
    // beforeEnter (to, from, next) {
    //   const isLogin = localStorage.isLogin
    //   if (isLogin) {
    //     next({ name: 'Home' })
    //   } else {
    //     next()
    //   }
    //   next()
    // }
  },
  {
    path: '/Register',
    name: 'Register',
    component: () => import(/* webpackChunkName: "Register" */ '../views/Register/Register.vue')
    // beforeEnter (to, from, next) {
    //   const isLogin = localStorage.isLogin
    //   if (isLogin) {
    //     next({ name: 'Home' })
    //   } else {
    //     next()
    //   }
    //   next()
    // }
  }
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})
// router.beforeEach((to, from, next) => {
//   const { isLogin } = localStorage
//   const { name } = to
//   const isLoginOrRegister = (name === 'Login' || name === 'Register');
//   (isLogin || isLoginOrRegister) ? next() : next({ name: 'Login' })
// })
export default router

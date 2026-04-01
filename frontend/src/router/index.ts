import { createRouter, createWebHistory } from 'vue-router'
import Layout from '@/components/Layout.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/views/Login.vue'),
    },
    {
      path: '/',
      component: Layout,
      redirect: '/dashboard',
      children: [
        {
          path: 'dashboard',
          name: 'Dashboard',
          component: () => import('@/views/Dashboard/index.vue'),
          meta: { title: '全局资源视图', icon: 'DataLine' },
        },
        {
          path: 'functions',
          name: 'Functions',
          component: () => import('@/views/Functions/index.vue'),
          meta: { title: '函数服务市场', icon: 'Collection' },
        },
        {
          path: 'workflow',
          name: 'Workflow',
          component: () => import('@/views/Workflow/index.vue'),
          meta: { title: '工作流编排', icon: 'Share' },
        },
        {
          path: 'monitor',
          name: 'Monitor',
          component: () => import('@/views/Monitor/index.vue'),
          meta: { title: '资源监控', icon: 'Monitor' },
        },
        {
          path: 'libraries',
          name: 'Libraries',
          component: () => import('@/views/Libraries/index.vue'),
          meta: { title: '数学库/求解器', icon: 'Cpu' },
        },
      ],
    },
  ],
})

export default router

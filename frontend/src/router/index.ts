import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TaskScheduler from '../views/TaskScheduler.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/task-scheduler',
    name: 'task-scheduler',
    component: TaskScheduler,
    meta: { title: '任务调度' }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

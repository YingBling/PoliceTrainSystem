import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'
// 静态路由:constantRoutes(全部成员可以访问)
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '首页', icon: 'dashboard' }
    }]
  }
]

// 动态路由:asyncRoutes(需要权限才能访问)
export const asyncRoutes = [
  {
    path: '/system',
    component: Layout,
    redirect: '/system/users',
    name: 'system',
    meta: { title: '系统管理', icon: 'system', role: ['超级用户'] },
    children: [
      {
        path: 'users',
        component: () => import('@/views/system/user/index'), // Parent router-view
        name: 'users',
        meta: { title: '用户管理', icon: 'user', role: ['超级用户'] }
      },
      {
        path: 'permission',
        component: () => import('@/views/system/role/index'),
        name: 'permission',
        meta: { title: '权限管理', icon: 'lock', role: ['超级用户'] }
      },
      {
        path: 'department',
        component: () => import('@/views/system/dept/index'),
        name: 'department',
        meta: { title: '部门管理', icon: 'tree', role: ['超级用户'] }
      },
      {
        path: 'post',
        component: () => import('@/views/system/post/index'),
        name: 'post',
        meta: { title: '岗位管理', icon: 'post', role: ['超级用户'] }
      }]
  },
  {
    path: '/lesson',
    component: Layout,
    redirect: '/lesson/study',
    name: 'system',
    meta: { title: '课程管理', icon: 'example', role: ['超级用户'] },
    children: [
      {
        path: 'study',
        component: () => import('@/views/lesson/study/index'),
        name: 'study',
        meta: { title: '课程学习', icon: 'education', role: ['超级用户'] }
      },
      {
        path: 'lessonSys',
        component: () => import('@/views/lesson/lessonSys/index'), // Parent router-view
        name: 'lessonSys',
        meta: { title: '课程设置', icon: 'form', role: ['超级用户'] },
      },
      {
        path: 'charpter',
        component: () => import('@/views/lesson/lessonSys/charpter'),
        name: 'charpter',
        meta: { title: '步骤2', icon: 'education', role: ['超级用户'] }
      },
      {
        path: 'lessonInfo',
        component: () => import('@/views/lesson/lessonSys/lessonInfo'),
        name: 'lessonInfo',
        meta: { title: '步骤1', icon: 'education', role: ['超级用户'] }
      },
      {
        path: 'publish',
        component: () => import('@/views/lesson/lessonSys/publish'),
        name: 'publish',
        meta: { title: '步骤3', icon: 'education', role: ['超级用户'] }
      },
      {
        path: 'categories',
        component: () => import('@/views/lesson/categories/index'), // Parent router-view
        name: 'Cate',
        meta: { title: '课程分类管理', icon: 'cate', role: ['超级用户'] }
      },
      {
        path: 'studyDetail',
        component: () => import('@/views/lesson/study/detail/studyDetail'),
        name: 'studyDetail',
        meta: { title: '课程详情', noCache: true, role: ['超级用户'] },
        hidden: true
      }]
  },
  {
    path: '/user',
    component: Layout,
    hidden: true,
    redirect: '/user/userInfo',
    children: [
      {
        path: 'userInfo',
        component: () => import('@/views/system/user/userInfo'),
        name: 'UserInfo',
        meta: { title: '个人中心', icon: 'user', role: ['超级用户'] }
      }
    ]
  },
  // 404 page must be placed at the end !!!
  // 注意 在constantRoutes 路由中不能定义404.它的层级会高于asyncRoutes 如果定义了你访问的时候只能访问到404页面。
  // 放在asyncRoutes 最后即可
  { path: '*', redirect: '/404', hidden: true }

]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router

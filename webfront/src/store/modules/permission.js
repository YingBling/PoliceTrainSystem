import { asyncRoutes, constantRoutes } from '@/router'
// 引入路由表
/**
 * Use meta.role to determine if the current user has permission
 * @param roles
 * @param route
 */
// 具体方法:
// 1:判断在路由mate中定义的roles是否包含用户角色返回的roles，对比筛选出来指定能访问的路由组装成数组返回
function hasPermission(roles, route) {
  if (route.meta && route.meta.roles) {
    return roles.some(role => route.meta.roles.includes(role))
  } else {
    return true
  }
}

/**
 * Filter asynchronous routing tables by recursion
 * @param routes asyncRoutes
 * @param roles
 */
export function filterAsyncRoutes(routes, roles) {
  const res = []
  // 循环定义的asyncRoutes权限的路由表
  routes.forEach(route => {
    const tmp = { ...route }
    if (hasPermission(roles, tmp)) {
      if (tmp.children) { // 如果有子项,进行递归过滤
        tmp.children = filterAsyncRoutes(tmp.children, roles)
      }
      res.push(tmp) // 如果定义的mate中roles包含用户roles中的某一项 则添加到res中
    }
  })

  return res
}
// 定义state
const state = {
  routes: [],
  addRoutes: []
}
// 创建mutations用于更改state
// 通过routes[],addrouters[]两个数组将筛选好的路由以及结合静态路由全部保存起来
const mutations = {
  SET_ROUTES: (state, routes) => {
    state.addRoutes = routes
    state.routes = constantRoutes.concat(routes)// 组合路由,将原始路由和权限路由组合生成路由表
  }
}

const actions = {
  // 这里是获取 权限路由 参数roles即用户信息中返回的roles（根据传过来的角色去筛选动态路由数组）
  generateRoutes({ commit }, roles) {
    return new Promise(resolve => {
      let accessedRoutes
      // if (roles.includes('admin')) {  //如果是管理员 直接返回定义的权限路由表
      //   accessedRoutes = asyncRoutes || []
      // } else {
      //   accessedRoutes = filterAsyncRoutes(asyncRoutes, roles) //不是就调用filterAsyncRoutes()方法过滤定义的权限路由表，返回有权限的路由
      // }
      // eslint-disable-next-line prefer-const
      accessedRoutes = filterAsyncRoutes(asyncRoutes, roles)
      commit('SET_ROUTES', accessedRoutes) // 更改state
      console.log(accessedRoutes)
      resolve(accessedRoutes) // 返回生成的权限路由表
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}

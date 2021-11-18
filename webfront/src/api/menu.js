import request from '@/utils/request'

// 获取路由
export function getRouters(token) {
  return request({
    url: 'api/rbac/user/get_menu_button/',
    method: 'get',
    params: {token}
  })
}

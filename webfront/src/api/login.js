import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/login/',
    method: 'post',
    data
  })
}

export function getInfo(id) {
  return request({
    url: '/api/rbac/users/' + id,
    method: 'get'
  })
}

export function logout() {
  return request({
    url: '/vue-admin-template/user/logout',
    method: 'post'
  })
}

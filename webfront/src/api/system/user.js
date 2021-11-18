import request from '@/utils/request';

// 查询用户列表
export function listUser(page, limit, query) {
  return request({
    url: '/api/rbac/user/',
    method: 'get',
    params: query
  })
}

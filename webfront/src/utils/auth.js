import Cookies from 'js-cookie'
// 该js文件为操作token的基础模板
const TokenKey = 'Authorization'
// 提供了获取token、设置token、删除token的方法，可以直接使用
export function getToken() {
  return sessionStorage.getItem(TokenKey)
}

export function setToken(token) {
  return sessionStorage.setItem(TokenKey, token)
}

export function removeToken() {
  return sessionStorage.removeItem(TokenKey)
}

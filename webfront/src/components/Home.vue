<template>
  <div class="Home">
    <h1>
      {{ msg }}
    </h1>
  </div>
</template>

<script>
export default {
  name: "Home",
  created() {
    // 刷新页面后调用created方法
    // 请求所有的用户数据
    this.$axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/user/all/',
      headers: {
        // 设置请求头中的Authorization字段，每次发起请求时携带token
        'Authorization': 'Bearer ' + localStorage.getItem('token')
      }
    })
      .then(resp => {
        if (resp.data['code'] === 200) {
          this.msg = resp.data
        } else {
          this.msg = '获取用户信息出错'
        }
      })
      .catch(err => {
        alert('请重新登录')
        this.$router.push('/')
        console.log(err)
      })

  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
    // changeMsg() {
    //   this.msg = 'Bye~'
    // },
    // func() {
    //   alert('created.')
    // }
  }
}
</script>

<style scoped>

</style>

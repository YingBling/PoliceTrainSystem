<template>
  <div id="userLayout">
    <div class="login_panle">
      <div class="login_panle_form">
        <div class="login_panle_form_title">
          <img class="login_panle_form_title_logo" src="../assets/images/logo_login.png" alt="">
          <p class="login_panle_form_title_p" style="font-family: 'Microsoft YaHei',serif">执法训练成绩评估综合管理平台</p>
        </div>
        <!--			 登录表单区域 -->
        <el-form
          ref="loginForm"
          :model="loginForm"
          :rules="loginRules"
          class="login-form">
          <!-- 用户名 -->
          <el-form-item prop="username">
            <el-input
              v-model="loginForm.username"
              type="text" auto-complete="off"
              placeholder="账号"
              prefix-icon="el-icon-user">
            </el-input>
          </el-form-item>
          <!-- 密码 -->
          <el-form-item prop="password">
            <el-input
              v-model="loginForm.password"
              type="password"
              auto-complete="off"
              placeholder="密码"
              prefix-icon="el-icon-lock"
              @keyup.enter.native="handleLogin"
            >
            </el-input>
          </el-form-item>
          <div/>
          <!-- 按钮区域-->
          <el-form-item style="width:100%;">
            <el-button
              :loading="loading"
              size="medium"
              type="primary"
              style="width:100%;"
              @click="handleLogin"
            >
              <span v-if="!loading">登 录</span>
              <span v-else>登 录 中...</span>
            </el-button>
          </el-form-item>
        </el-form>
      </div>
      <div class="login_panle_right"/>
      <!--  底部区域  -->
      <div class="login_panle_foot">
        <div class="el-login-footer">
          <span>Copyright © 2020-2021  All Rights Reserved.</span> |
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data() {
    return {
      // 登录表单的数据绑定对象
      loginForm: {
        username: "sm",
        password: "12345"
      },
      // 表单的验证规则对象
      loginRules: {
        // 验证用户名是否合法
        // required 是否为必填项
        // message 当前规则校验失败时的提示
        // trigger 表单验证的触发实际，blur表示失去焦点时触发
        username: [
          {required: true, trigger: "blur", message: "用户名不能为空"}
        ],
        password: [
          {required: true, trigger: "blur", message: "密码不能为空"}
        ]
      },
      loading: false,
    }
  },
  methods: {
    saveObj(key, obj) {
      let jsonstr = JSON.stringify(obj)
      sessionStorage.setItem(key, jsonstr)
    },
    getObj(key) {
      return JSON.parse(sessionStorage.getItem(key))
    },
    //登录
    handleLogin() {
      const self = this
      if (self.loginForm.username !== '' && self.loginForm.password !== '') {
        self.$axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/api/login/',
          data: {
            username: self.loginForm.username,
            password: self.loginForm.password
          }
        })
          .then(res => {
            if (res.data['code'] === 200) {
              this.$message({
                type: 'success',
                message: '登录成功'
              })
              sessionStorage.setItem('username', res.data['data']['username'])
              sessionStorage.setItem('uid', res.data['data']['id'])
              sessionStorage.setItem('refresh', res.data['data']['refresh'])
              sessionStorage.setItem('access', res.data['data']['access'])
              this.$router.push('/index')
            } else {
              this.$message({
                type: 'error',
                message: '用户名或密码错误'
              })
            }
          }).catch(err => {
            this.$message({
              type: 'error',
              message: '服务器错误'
            })
          }
        )
      } else {
        this.$message({
          type: 'error',
          message: '用户名或密码为空'
        })
      }
    },
  }
}
</script>

<style lang="scss" scoped>
#userLayout {
  margin: 0;
  padding: 0;
  background-image: url("../assets/images/login_background.svg");
  background-size: cover;
  width: 100%;
  height: 100%;
  position: relative;

  .login_panle {
    position: absolute;
    top: 3vh;
    left: 2vw;
    width: 96vw;
    height: 94vh;
    background-color: rgba(255, 255, 255, .8);
    backdrop-filter: blur(5px);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: space-evenly;

    .login_panle_right {
      background-image: url("../assets/images/login_left.svg");
      background-size: cover;
      width: 40%;
      height: 60%;
      float: right !important;
    }

    .login_panle_form {
      width: 420px;
      background-color: #fff;
      padding: 40px 40px 40px 40px;
      border-radius: 10px;
      box-shadow: 2px 3px 7px rgba(0, 0, 0, .2);

      .login_panle_form_title {

        display: flex;
        align-items: center;
        margin: 30px 0;

        .login_panle_form_title_logo {
          width: 90px;
          height: 72px;
        }

        .login_panle_form_title_p {
          font-size: 40px;
          padding-left: 20px;
        }
      }
    }

    .login_panle_foot {
      position: absolute;
      bottom: 20px;
    }
  }
}

/*//小屏幕不显示右侧，将登陆框居中*/
@media (max-width: 750px) {
  .login_panle_right {
    display: none;
  }
  .login_panle {
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
  }
  .login_panle_form {
    width: 100%;
  }
}
</style>

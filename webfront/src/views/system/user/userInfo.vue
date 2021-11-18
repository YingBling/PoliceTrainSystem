<template>
  <div class="app-container">
    <el-row :gutter="20">
      <el-col :span="6" :xs="24">
        <el-card class="personal-info">
          <div class="user-avatars">
             <img src="https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png" >
          </div>
          <ul class="info-list">
            <li class="list-group-item">
              <div class="list-group-item-p">
                <svg-icon icon-class="user"/>
                <span>用户名</span>
                <div class="pull-right">{{ user.username }}</div>
              </div>
            </li>
            <li class="list-group-item">
              <div class="list-group-item-p">
                <svg-icon icon-class="phone" />
                <span>手机号码</span>
                <div class="pull-right">{{ user.mobile }}</div>
              </div>
            </li>
            <li class="list-group-item">
              <div class="list-group-item-p">
                <svg-icon icon-class="email" />
                <span>用户邮箱</span>
                <div class="pull-right">{{ user.email }}</div>
              </div>
            </li>
            <li class="list-group-item">
              <div class="list-group-item-p">
                <svg-icon icon-class="tree" />
                <span>部门</span>
                <div v-if="user.dept" class="pull-right">{{ user.dept.deptName }}/{{ user.postName }}</div>
              </div>
            </li>
            <li class="list-group-item">
              <div class="list-group-item-p">
                <svg-icon icon-class="peoples" />
                <span style="margin-left: 4px">角色</span>
                <div class="pull-right">{{ user.roleName }}</div>
              </div>
            </li>
          </ul>
        </el-card>
      </el-col>
      <el-col :span="18" :xs="24">
        <el-card class="modify-info">
          <el-tabs>
            <el-tab-pane label="基本资料" name="userinfo">
              <el-form ref="form" :model="user" :rules="rules" label-width="80px">
                <el-form-item label="用户名" prop="username">
                  <el-input v-model="user.username" />
                </el-form-item>
                <el-form-item label="手机号码" prop="mobile">
                  <el-input v-model="user.mobile" />
                </el-form-item>
                <el-form-item label="邮箱" prop="email">
                  <el-input v-model="user.email" />
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" size="mini">保存</el-button>
                </el-form-item>
              </el-form>
            </el-tab-pane>
            <el-tab-pane label="修改密码" name="resetPwd">
              <el-form ref="form" :model="user" :rules="rules" label-width="80px">
                <el-form-item label="旧密码" prop="oldPassword">
                  <el-input v-model="user.oldPassword" placeholder="请输入旧密码" type="password" />
                </el-form-item>
                <el-form-item label="新密码" prop="newPassword">
                  <el-input v-model="user.newPassword" placeholder="请输入新密码" type="password" />
                </el-form-item>
                <el-form-item label="确认密码" prop="confirmPassword">
                  <el-input v-model="user.confirmPassword" placeholder="请确认密码" type="password" />
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" size="mini">保存</el-button>
                </el-form-item>
              </el-form>
            </el-tab-pane>
          </el-tabs>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'UserInfo',
  data() {
    const equalToPassword = (rule, value, callback) => {
      if (this.user.newPassword !== value) {
        callback(new Error('两次输入密码不一致'))
      } else {
        callback()
      }
    }
    return {
      user: {
        username: 'admin',
        mobile: null,
        email: 'admin@qq.com',
        dept: {
          deptName: '信息学院'
        },
        postName: '学生',
        roleName: '管理员',
        oldPassword: undefined,
        newPassword: undefined,
        confirmPassword: undefined
      },
      rules: {
        username: [
          { required: true, message: '用户昵称不能为空', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '邮箱地址不能为空', trigger: 'blur' },
          {
            type: 'email',
            message: "'请输入正确的邮箱地址",
            trigger: ['blur', 'change']
          }
        ],
        mobile: [
          { required: true, message: '手机号码不能为空', trigger: 'blur' },
          {
            pattern: /^1[3|4|5|6|7|8|9][0-9]\d{8}$/,
            message: '请输入正确的手机号码',
            trigger: 'blur'
          }
        ],
        oldPassword: [
          { required: true, message: '旧密码不能为空', trigger: 'blur' }
        ],
        newPassword: [
          { required: true, message: '新密码不能为空', trigger: 'blur' },
          { min: 6, max: 20, message: '长度在 6 到 20 个字符', trigger: 'blur' }
        ],
        confirmPassword: [
          { required: true, message: '确认密码不能为空', trigger: 'blur' },
          { required: true, validator: equalToPassword, trigger: 'blur' }
        ]
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.el-card{
  min-height: 520px;
}
.user-avatars {
  //margin: 0 auto;
  overflow: hidden;
  text-align: center;
  margin-top: 20px;
  margin-bottom: 20px;
}
.info-list {
  padding: 0px;
  list-style: none;
  font-family: "Microsoft YaHei";
  font-size: 14px;
}
.list-group-item{
  line-height: 46px;
}
.list-group-item-p{
  margin-top: 0;
  margin-bottom: 1em;
}
.svg-icon{
  margin-right: 10px;
  font-size: 18px;
}
//.list-group-item {
//  border-bottom: 1px solid #e7eaec;
//  border-top: 1px solid #e7eaec;
//  margin-bottom: -1px;
//  padding: 11px 0px;
//  font-size: 13px;
//}
.pull-right {
  float: right !important;
}

</style>

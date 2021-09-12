<template>
  <div>
    <div style=""><el-avatar shape="square" :size="150" :fit="fit" src="https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png"></el-avatar></div>

  <el-form ref="form" :model="formLabelAlign" label-width="auto" :label-position="left">
    <el-form-item label="用户编号：">
      <el-input v-model="userInfo.id" disabled="True" style="width: auto">
      </el-input>
    </el-form-item>
    <el-form-item label="用户名：">
      <el-input v-model="userInfo.username"
                disabled="True"
                style="width: auto">
      </el-input>
    </el-form-item>
    <el-form-item label="姓名：">
      <el-input v-model="userInfo.name"
                style="width: auto">
      </el-input>
    </el-form-item>
    <el-form-item label="所属部门：">
      <el-input v-model="userInfo.dept_name" disabled="True" style="width: auto">
      </el-input>
    </el-form-item>
    <el-form-item label="关联角色：">
      <el-tag
        v-for="role in userInfo.roles_list"
        style=""
        type="success"
      >
        {{ role }}
      </el-tag>

    </el-form-item>
    <el-form-item label="用户状态：">
      <el-switch v-model="userInfo.is_active" disabled="True"></el-switch>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="onSubmit">更新资料</el-button>
    </el-form-item>
  </el-form>
    </div>
</template>

<script>
export default {
  name: "Info",
  data() {
    return {
      userInfo: null,
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: '',
      },
    }
  },
  created() {
    let id = this.$route.params['id']
    this.$axios({
      method: "GET",
      url: `http://127.0.0.1:8000/api/rbac/users/${id}`
    }).then(res => {
      this.userInfo = res.data
    })
  }
}

</script>

<style scoped>

</style>

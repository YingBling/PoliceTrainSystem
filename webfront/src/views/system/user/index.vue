<template>
  <div class="app-container">
    <el-card>
      <el-row :gutter="20">
        <el-col :span="36" :xs="24">
           <!-- 搜索框 -->
          <el-form ref="queryForm" :model="queryParams" :inline="true" label-width="68px">
            <el-form-item label="账号" prop="username">
              <el-input
                v-model="queryParams.username"
                placeholder="请输入账号"
                clearable
                size="small"
                style="width: 240px"
                @keyup.enter.native="handleQuery"
              />
            </el-form-item>
            <el-form-item label="姓名" prop="name">
              <el-input
                v-model="queryParams.name"
                placeholder="请输入姓名"
                clearable
                size="small"
                style="width: 240px"
                @keyup.enter.native="handleQuery"
              />
            </el-form-item>
            <el-form-item label="状态" prop="is_active">
<!--              数据库中状态一栏应是0或者1，这样才能根据:value修改状态栏-->
              <el-select
                v-model="queryParams.is_active"
                placeholder="请选择"
                clearable
                size="small"
                style="width: 240px"
              >
                <el-option
                  label="正常"
                  :value="1"
                />
                <el-option
                  label="停用"
                  :value="0"
                />
              </el-select>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
              <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
            </el-form-item>
          </el-form>
          <!--增删导入导出按钮-->
          <el-row :gutter="10" class="mb8">
            <el-col :span="1.5">
              <el-button
                type="primary"
                plain
                icon="el-icon-plus"
                size="mini"
                @click="handleAdd"
              >新增
              </el-button>
            </el-col>
            <el-col :span="1.5">
              <el-button
                type="danger"
                plain
                icon="el-icon-delete"
                size="mini"
                :disabled="multiple"
                @click="handleDelete"
              >删除
              </el-button>
            </el-col>
            <el-col :span="1.5">
              <el-button
                type="info"
                plain
                icon="el-icon-upload2"
                size="mini"
                @click="handleImport"
              >导入
              </el-button>
            </el-col>
            <el-col :span="1.5">
              <el-button
                type="warning"
                plain
                icon="el-icon-download"
                size="mini"
                @click="handleExport"
              >导出
              </el-button>
            </el-col>
          </el-row>
          <!--用户列表区域-->
          <el-table :data="userList" height="400" style="width: 100%" @selection-change="handleSelectionChange">
            <el-table-column type="selection" width="50" align="center" />
            <el-table-column key="id" sortable label="用户编号" align="center" prop="id" />
            <el-table-column
              key="username"
              label="用户账号"
              align="center"
              prop="username"
              :show-overflow-tooltip="true"
            />
            <el-table-column
              key="name"
              label="姓名"
              align="center"
              prop="name"
              :show-overflow-tooltip="true"
            />
            <el-table-column
              key="gender"
              label="性别"
              align="center"
              :show-overflow-tooltip="true"
            >
              <template slot-scope="scope">
                <span v-if="scope.row.gender">男</span>
                <span v-else>女</span>
              </template>
            </el-table-column>
            <el-table-column
              key="role"
              label="角色"
              align="center"
              :show-overflow-tooltip="true"
            >
              <template slot-scope="scope">
                <template v-if="scope.row.role_list.length > 0">
                  <span v-for="item in scope.row.role_list">
                    {{ item }}
                  </span>
                </template>
                <template v-else>
                  <span>暂无角色</span>
                </template>
              </template>
            </el-table-column>
            <el-table-column
              key="is_active"
              label="状态"
              align="center"
            >
              <template slot-scope="scope">
                <!--              scope.row代表该行所有数据-->
                <el-switch
                  v-model="scope.row.is_active"
                  disabled
                  @change="handleStatusChange(scope.row)"
                />
              </template>
            </el-table-column>
            <el-table-column
              label="创建时间"
              align="center"
              prop="create_time"
              width="160"
            />
            <el-table-column
              label="操作"
              align="center"
              width="180"
              fixed="right"
              class-name="small-padding fixed-width"
            >
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  type="primary"
                  icon="el-icon-edit"
                  @click="handleUpdate(scope.row)"
                />
                <el-button
                  v-if="scope.row.id !== 1"
                  size="mini"
                  type="danger"
                  icon="el-icon-delete"
                  @click="handleDelete(scope.row.id)"
                />
                <el-tooltip effect="light" content="重置" placement="bottom" :enterable="false">
                  <el-button
                    size="mini"
                    type="warning"
                    icon="el-icon-key"
                    @click="handleResetPwd(scope.row)"
                  />
                </el-tooltip>
              </template>
            </el-table-column>
          </el-table>
          <!--   分页区-->
<!--          <div class="pagination-container">-->
<!--            <el-pagination-->
<!--              :current-page="queryParams.pageNum"-->
<!--              :page-size="queryParams.pageSize"-->
<!--              layout='total, prev, pager, next, jumper'-->
<!--              :total="total"-->
<!--              style="text-align: right;margin-top: 30px"-->
<!--              @current-change="getList"/>-->
<!--          </div>-->
          <!-- 分页区域 -->
          <!--          page	当前页数  支持 .sync 修饰符	-->
          <!--          limit	每页显示条目个数-->
          <pagination
            v-show="total>0"
            :total="total"
            :page.sync="queryParams.pageNum"
            :limit.sync="queryParams.pageSize"
            @pagination="getList"
          />
        </el-col>
      </el-row>
    </el-card>
    <!--  添加或修改参数配置对话框  -->
    <el-dialog :title="title" :visible.sync="open" width="600px" append-to-body>
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <el-row>
          <el-col :span="12">
            <el-form-item label="姓名" prop="name">
              <el-input v-model="form.name" placeholder="请输入用户昵称" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="角色">
              <el-select v-model="form.roleIds" multiple placeholder="请选择">
                <el-option
                  v-for="item in roleOptions"
                  :key="item.id"
                  :label="item.roleName"
                  :value="item.id"
                  :disabled="item.status == 0"
                />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="手机号码" prop="mobile">
              <el-input v-model="form.mobile" placeholder="请输入手机号码" maxlength="11" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="邮箱" prop="email">
              <el-input v-model="form.email" placeholder="请输入邮箱" maxlength="50" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item v-if="form.id == undefined" label="用户名称" prop="username">
              <el-input v-model="form.username" placeholder="请输入用户名称" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item v-if="form.id == undefined" label="用户密码" prop="password">
              <el-input v-model="form.password" placeholder="请输入用户密码" type="password" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="性别">
              <el-select v-model="form.gender" placeholder="请选择">
                <el-option
                  v-for="dict in sexOptions"
                  :key="dict.dictValue"
                  :label="dict.dictLabel"
                  :value="dict.dictValue"
                />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="状态">
              <el-radio-group v-model="form.is_active">
                <el-radio
                  v-for="dict in statusOptions"
                  :key="dict.dictValue"
                  :label="dict.dictValue"
                >{{ dict.dictLabel }}
                </el-radio>
              </el-radio-group>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="24">
            <el-form-item label="备注">
              <el-input v-model="form.remark" type="textarea" placeholder="请输入内容" />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitForm">确 定</el-button>
        <el-button @click="cancel">取 消</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
import { listUser } from '@/api/system/user'
import Pagination from '@/components/Pagination'
export default {
  name: 'User',
  components: { Pagination },
  data() {
    return {
      // 非多个禁用
      multiple: false,
      // 选中数组
      ids: [],
      // 总条数
      total: 0,
      // 用户表格数据
      userList: null,
      // 弹出层标题
      title: '',
      // 是否显示弹出层
      open: false,
      // 状态数据字典
      statusOptions: [{ dictLabel: '正常', dictValue: true }, { dictLabel: '停用', dictValue: false }],
      // 表单参数
      form: {},
      // 查询参数
      queryParams: {
        pageNum: 1,
        pageSize: 10,
        username: undefined,
        name: undefined,
        is_active: undefined
      },
      // 表单校验
      rules: {
        username: [
          { required: true, message: '用户名不能为空', trigger: 'blur' }
        ],
        name: [
          { required: true, message: '姓名不能为空', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '用户密码不能为空', trigger: 'blur' }
        ],
        email: [
          {
            type: 'email',
            message: '请输入正确的邮箱地址',
            trigger: ['blur', 'change']
          }
        ],
        mobile: [
          {
            pattern: /^1[3|4|5|6|7|8|9][0-9]\d{8}$/,
            message: '请输入正确的手机号码',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    // 查询用户列表
    getList() {
      listUser(this.queryParams).then(res => {
        console.log(res)
        this.userList = res.results
        this.total = res.count
      })
    },
    // 多选框选中数据
    handleSelectionChange(selection) {
      this.ids = selection.map(item => item.id)
      this.multiple = !selection.length
    },
    // 搜索按钮功能
    handleQuery() {
      this.getList()
    },
    // 重置按钮：清空搜索栏
    resetQuery() {
      // 1.表单输入项数据清空
      this.queryParams = {}
      // 2.查询所有数据
      this.getList()
    },
    // 用户状态修改
    handleStatusChange(row) {
      const text = row.is_active === true ? '启用' : '停用'
      this.$confirm('确认要"' + text + '""' + row.username + '"用户吗?', '警告', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(function() {
        // 修改用户状态的接口？？？
        return changeUserStatus(row.id, row.is_active)
      }).then(() => {
        this.msgSuccess(text + '成功')
      }).catch(function() {
        row.is_active = row.is_active === false
      })
    },
    // 新增用户
    handleAdd() {
      this.open = true
      this.title = '添加用户'
    },
    // 修改用户信息
    handleUpdate(row) {
      this.open = true
      this.title = '修改用户'
    },
    // 删除用户
    handleDelete() {
    },
    // 用户导入
    handleExport() {
    },
    // 用户导出
    handleImport() {
    },
    // 重置用户密码
    handleResetPwd(row) {
    }
  }
}
</script>

<style scoped>

</style>

<template>
<div class="app-container">
<!--  面包屑导航-->
  <el-breadcrumb separator-class="el-icon-arrow-right">
<!--      <el-breadcrumb-item v-for="(item,i) in data" :key="item" :to="getPath(i)">{{item}}</el-breadcrumb-item>-->
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
  </el-breadcrumb>
<!--  卡片视图区域-->
    <el-card>
      <el-row :gutter="20">
      <!-- 搜索框 -->
       <el-col :span="36" :xs="24">
        <el-form :inline="true" label-width="68px">
          <el-form-item label="账号" prop="userid">
            <el-input
              placeholder="请输入账号"
              clearable
              size="small"
              style="width: 240px"
              @keyup.enter.native="handleQuery"
            />
          </el-form-item>
          <el-form-item label="姓名" prop="username">
            <el-input
              placeholder="请输入姓名"
              clearable
              size="small"
              style="width: 240px"
              @keyup.enter.native="handleQuery"
            />
          </el-form-item>
          <el-form-item label="部门" prop="dept">
            <el-select
              placeholder="请选择"
              clearable
              size="small"
              style="width: 240px"
            >
            <el-option label="企划" ></el-option>
            <el-option label="人力" ></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="状态" prop="is_active">
            <el-select
              placeholder="请选择"
              clearable
              size="small"
              style="width: 240px"
            >
              <el-option label="启动" value="on"></el-option>
              <el-option label="禁用" value="off"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
            <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
          </el-form-item>
        </el-form>
      <!--增删改导入按钮-->
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
              type="success"
              plain
              icon="el-icon-edit"
              size="mini"
              @click="handleUpdate"
            >修改
            </el-button>
          </el-col>
          <el-col :span="1.5">
            <el-button
              type="danger"
              plain
              icon="el-icon-delete"
              size="mini"
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
        <el-table :data="userList.users" @selection-change="handleSelectionChange">
          <el-table-column type="selection" width="50" align="center" />
          <el-table-column key="id" label="序号" align="center" prop="id" />
          <el-table-column
            key="userid" label="用户账号" align="center" prop="userid"
            :show-overflow-tooltip="true"
          />
          <el-table-column key="username" label="用户姓名"
            align="center"
            prop="username"
            :show-overflow-tooltip="true"
          />
          <el-table-column
            key="dept"
            label="部门"
            align="center"
            prop="dept"
            :show-overflow-tooltip="true"
          />
          <el-table-column
            key="role"
            label="角色"
            align="center"
            prop="role"
            :show-overflow-tooltip="true"
          >
          </el-table-column>
          <el-table-column
            key="mobile"
            label="手机号码"
            align="center"
            prop="mobile"
            width="120"
          />
          <el-table-column
            key="is_active" label="状态" align="center">
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
            label="创建时间" align="center" prop="create_time" width="160">
          </el-table-column>
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
              >
              </el-button>
              <el-button
                v-if="scope.row.id !== 1"
                size="mini"
                type="danger"
                icon="el-icon-delete"
                @click="handleDelete(scope.row)"
              >
              </el-button>
              <el-tooltip  effect="light" content="重置" placement="bottom" :enterable="false">
              <el-button
                size="mini"
                type="warning"
                icon="el-icon-key"
                @click="handleResetPwd(scope.row)"
              >
              </el-button>
              </el-tooltip>
            </template>
          </el-table-column>
        </el-table>

         <!-- 分页区域 -->
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="queryInfo.pagenum"
          :page-sizes="[1,2,5,10]"
          :page-size="queryInfo.pagesize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="queryInfo.totalpage"
        ></el-pagination>
      </el-col>
      </el-row>
    </el-card>
</div>
</template>

<script>
export default {
  name: "user",
  data() {
    return {
      queryInfo:{
        "totalpage": 5,
        //当前页数
        "pagenum": 4,
        // 当前每页显示多少条数据
        "pagesize":2,
      },
      userList:{
        "users":[
            {
                "id": 25,
                "userid":2020210345,
                "username": "summer",
                "mobile": "18616358651",
                "email": "tige112@163.com",
                "dept": "人力资源",
                "is_active": true, // 当前用户的状态
                "role": "炒鸡管理员",
                "create_time": "2017-11-09 20:36:26",
            },
            {
                "id":23,
                "userid":2020210355,
                "username": "sid",
                "mobile": "13489303480",
                "email": "tsdhf@163.com",
                "dept": "财务",
                "is_active": false, // 当前用户的状态
                "role": "普通用户",
                "create_time": "2021-08-09 10:06:26",
            }
        ]
       },
    }
  },
  methods: {
    handleSizeChange(newSize){
      this.queryInfo.pagesize=newSize
    }

  }
};
</script>

<style lang="scss" scoped>
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
}
</style>

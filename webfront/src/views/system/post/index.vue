<template>
  <div class="app-container">
<!--    搜索框-->
    <el-form ref="queryForm" :model="queryParams" :inline="true" label-width="68px">
      <el-form-item label="岗位编码" prop="postCode">
        <el-input
          v-model="queryParams.postCode"
          placeholder="请输入岗位编码"
          clearable
          size="small"
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="岗位名称" prop="postName">
        <el-input
          v-model="queryParams.postName"
          placeholder="请输入岗位名称"
          clearable
          size="small"
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="状态" prop="status">
        <el-select v-model="queryParams.status" placeholder="岗位状态" clearable size="small">
          <el-option label="1" value="1"></el-option>
          <el-option label="0" value="0"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form>
<!--    功能按钮-->
    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button
          type="primary"
          plain
          icon="el-icon-plus"
          size="mini"
          @click="handleAdd"
        >新增</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="success"
          plain
          icon="el-icon-edit"
          size="mini"
          :disabled="single"
          @click="handleUpdate"
        >修改</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="danger"
          plain
          icon="el-icon-delete"
          size="mini"
          :disabled="multiple"
          @click="handleDelete"
        >删除</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="warning"
          plain
          icon="el-icon-download"
          size="mini"
          @click="handleExport"
        >导出</el-button>
      </el-col>
    </el-row>
<!--    表单数据-->
    <el-table :data="postList" @selection-change="handleSelectionChange" style="padding-top: 20px">
      <el-table-column type="selection" width="55" align="center" />
      <el-table-column label="岗位编号" align="center" prop="id" />
      <el-table-column label="岗位编码" align="center" prop="postCode" />
      <el-table-column label="岗位名称" align="center" prop="postName" />
      <el-table-column label="岗位排序" align="center" prop="postSort" />
      <el-table-column label="状态" align="center" prop="status"  />
      <el-table-column label="创建时间" align="center" prop="create_datetime" width="180" />
      <el-table-column
        label="操作"
        align="center"
        class-name="small-padding fixed-width"
      >
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleUpdate(scope.row)"
          >修改</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-delete"
            @click="handleDelete(scope.row)"
          >删除</el-button>
        </template>
      </el-table-column>
    </el-table>
<!--    分页区域-->
    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="queryParams.pageNum"
      :limit.sync="queryParams.pageSize"
      @pagination="getPostList"
    />
  </div>
</template>

<script>
export default {
  name: 'Post',
  data() {
    return {
      // 查询参数
      queryParams: {
        pageNum: 1,
        pageSize: 10,
        postCode: undefined,
        postName: undefined,
        status: undefined
      },
      // 表单参数
      postList: [{
        'id': 1,
        'postCode': 'ceo',
        'postName': '局长',
        'postSort': 1,
        'status': '正常',
        'create_datetime': '2021/09/10 23:20'
      }, {
        'id': 2,
        'postCode': 'ce',
        'postName': '副局长',
        'postSort': 2,
        'status': '正常',
        'create_datetime': '2021/09/12 23:20'
      }, {
        'id': 3,
        'postCode': 'hr',
        'postName': '警员',
        'postSort': 1,
        'status': '正常',
        'create_datetime': '2021/09/13 23:20'
      }]
    }
  },
  methods: {
    getPostList() {
    },
    handleQuery() {
      this.queryParams.pageNum = 1
      this.getPostList()
    },
    /** 重置按钮操作 */
    resetQuery() {
    },
    // 多选框选中数据
    handleSelectionChange(selection) {
    },
    /** 新增按钮操作 */
    handleAdd() {},
    /** 修改按钮操作 */
    handleUpdate(row) {},
    /** 删除按钮操作 */
    handleDelete(row) {},
    /** 导出按钮操作 */
    handleExport() {}
  }
}
</script>

<style scoped>

</style>

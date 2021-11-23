<template>
  <div class="app-container">
<!--    卡片视图-->
    <el-card>
      <el-row style="padding-bottom: 20px">
        <el-col>
          <el-button type="primary" @click="showAddCateDialog">添加分类</el-button>
        </el-col>
      </el-row>
<!--      表格-->
      <tree-table
        :data ="catelist"
        :columns="columns"
        :selection-type="false"
        :expand-type="false"
        show-index
        index-text="#"
        border>
        <template slot="ok" slot-scope="scope">
          <i class="el-icon-success" v-if="scope.row.cat_deleted === false" style="color: lightgreen"></i>
          <i class="el-icon-error" v-else style="color: red"></i>
        </template>
        <template slot="order" slot-scope="scope">
          <el-tag size="mini" v-if="scope.row.cat_level===0" >一级</el-tag>
          <el-tag type="success" size="mini" v-else-if="scope.row.cat_level===1">二级</el-tag>
          <el-tag type="warning" size="mini" v-else>三级</el-tag>
        </template>
        <template slot="opt" slot-scope="scope">
          <el-button type="primary" icon="el-icon-edit" size="mini">编辑</el-button>
          <el-button type="danger" icon="el-icon-delete" size="mini">删除</el-button>
        </template>
      </tree-table>
<!--      分页区域-->
      <pagination
        v-show="total>0"
        :total="total"
        :page.sync="queryParams.pageNum"
        :limit.sync="queryParams.pageSize"
        @pagination="getCate"
      />
    </el-card>
<!--    添加分类的对话框-->
    <el-dialog
      title="添加分类"
      :visible.sync="addCateDialogVisible"
      width="30%">
<!--      添加分类的表单-->
      <el-form :model="addCateForm" :rules="addCateFormRules" ref="addCateFormRef" label-width="100px">
        <el-form-item label="分类名称" prop="cat_name">
          <el-input v-model="addCateForm.cat_name"></el-input>
        </el-form-item>
        <el-form-item label="父级分类">
          <el-cascader
            v-model="selectedKeys"
            :options="parentCateList"
            :props="cascaderProps"
             @change="parentCateChange"></el-cascader>
        </el-form-item>
      </el-form>
  <span slot="footer" class="dialog-footer">
    <el-button @click="addCateDialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="addCateDialogVisible = false">确 定</el-button>
  </span>
</el-dialog>
  </div>
</template>

<script>
import Pagination from '@/components/Pagination'
export default {
  name: 'Cate',
  components: { Pagination },
  data() {
    return {
      total: 5,
      queryParams: {
        pageNum: 1,
        pageSize: 10
      },
      // 分类的数据列表
      catelist: [
        { 'cat_id': 1,
          'cat_name': 'python',
          'cat_pid': 0,
          'cat_level': 0,
          'cat_deleted': false,
          'children': [{
            'cat_id': 3,
            'cat_name': '入门课程',
            'cat_pid': 1,
            'cat_level': 1,
            'cat_deleted': false,
            'children': [{
              'cat_id': 5,
              'cat_name': '科目1',
              'cat_pid': 3,
              'cat_level': 2,
              'cat_deleted': false
            }]
          }]
        },
        { 'cat_id': 2,
          'cat_name': 'Java',
          'cat_pid': 0,
          'cat_level': 0,
          'cat_deleted': false,
          'children': [{
            'cat_id': 4,
            'cat_name': '入门课程',
            'cat_pid': 2,
            'cat_level': 1,
            'cat_deleted': false,
            'children': [
              {
                'cat_id': 6,
                'cat_name': '科目1',
                'cat_pid': 4,
                'cat_level': 2,
                'cat_deleted': false
              }]
          }]
        }
      ],
      columns: [
        {
          label: '分类名称',
          prop: 'cat_name'
        }, {
          label: '是否有效',
          type: 'template',
          template: 'ok'
        }, {
          label: '排序',
          type: 'template',
          template: 'order'
        }, {
          label: '操作',
          type: 'template',
          template: 'opt'
        }
      ],
      // 控制添加分类对话框显示与隐藏
      addCateDialogVisible: false,
      addCateForm: {
        cat_id: '',
        cat_name: '',
        cat_pid: '',
        cat_level: ''
      },
      addCateFormRules: {
        cat_name: [
          { required: true, message: '请输入分类名称', trigger: 'blur' }]
      },
      // 父级分类列表
      parentCateList: [
        {
          cat_id: 23,
          cat_name: 'python',
          cat_pid: '0',
          cat_level: '1',
          children: {
            cat_id: 26,
            cat_name: 'python入门',
            cat_pid: '23',
            cat_level: '2'
          }
        }, {
          cat_id: 24,
          cat_name: 'java',
          cat_pid: '0',
          cat_level: '1',
          children: {
            cat_id: 27,
            cat_name: 'java入门',
            cat_pid: '24',
            cat_level: '2'
          }
        }, {
          cat_id: 25,
          cat_name: 'vue',
          cat_pid: '0',
          cat_level: '1',
          children: {
            cat_id: 28,
            cat_name: 'vue入门',
            cat_pid: '25',
            cat_level: '2'
          }
        }],
      // 指定级联选择器的配置对象
      cascaderProps: {
        expandTrigger: 'hover',
        value: 'cat_id',
        label: 'cat_name',
        children: [{
          value: 'children.cat_id',
          label: 'children.cat_name'
        }]
      },
      // 选中的父级分类的Id数组
      selectedKeys: []
    }
  },
  methods: {
    getCate() { },
    showAddCateDialog() {
      this.addCateDialogVisible = true
    },
    parentCateChange() {
      console.log(this.selectedKeys)
    }
  }
}
</script>

<style scoped>

</style>

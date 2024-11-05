<template>
    <div class="login-container">
        <el-card class="box-card">
            <div class="login-body">
                <div class="login-title">Django+Vue图书管理系统</div>
                <el-form ref="form" :model="userForm">
                    <el-input placeholder="请输入账号..." v-model="userForm.accountNumber" class="login-input">

                    </el-input>
                    <el-input placeholder="请输入密码..." v-model="userForm.userPassword" class="login-input"
                        @keyup.enter.native="login" show-password>

                    </el-input>

                    <el-select v-model="userForm.value" clearable placeholder="请选择" class="login-input">
                        <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                        </el-option>
                    </el-select>

                    <div class="login-submit">
                        <el-button type="primary" @click="login">登录</el-button>
                        <el-button type="warning" @click="$router.push('/register')" style="margin-left: 20px">注册</el-button>
                    </div>
                    <!-- <div class="other-submit">
                      <router-link to="/login-admin" class="sign-in-text">管理员登录</router-link>
                  </div> -->
                </el-form>
            </div>
        </el-card>
    </div>
</template>

<script>
export default {
    name: "login",
    data() {
        return {
            userForm: {
                accountNumber: 'admin',
                userPassword: 'admin',

            },
            options: [
                {
                    value: '1',
                    label: '管理员'
                },
                {
                    value: '2',
                    label: '老板'
                },
                {
                    value: '3',
                    label: '用户'
                }],
        };
    },

    methods: {
        login() {
            this.$request.post("/login/", {
                username: this.userForm.accountNumber,
                password: this.userForm.userPassword,
                value: this.userForm.value
            }).then(res => {
                console.log(res);
                if (res.data.meta.status === 200) {
                    localStorage.setItem("userInfo", res.data.data.username);
                    localStorage.setItem("userInfoid", res.data.data.user_id);
                    localStorage.setItem("img_url_touxiang", res.data.data.img_url);
                    localStorage.setItem("jianjie", res.data.data.jianjie);
                    localStorage.setItem("isAdmin", res.data.data.isAdmin);
                    localStorage.setItem("token", res.data.data.token);
                    this.$message.success("登陆成功")
                    if (this.userForm.value == 3) {
                        // localStorage.setItem("token", 'user')
                        this.$router.push('/home/index')
                        return
                    }
                    if (res.data.data.isAdmin == 1) { this.$router.replace({ path: '/media/list' }); }
                    else { this.$router.push('/media/list') }
                } else {
                    this.$message.error(res.data.meta.message);
                }
            });
        },
        toIndex() {
            this.$router.replace({ path: '/index' });
        }
    }
}
</script>

<style scoped>
.login-container {
    background-image: url('/src/assets/bj.jpg'); /* 替换为你的图片路径 */
    background-size: cover; /* 背景图片覆盖整个元素 */
    background-position: center; /* 背景图片居中 */
    background-repeat: no-repeat; /* 不重复背景图片 */
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100%;

}

.login-body {
    padding: 30px;
    width: 300px;
    height: 100%;
}

.login-title {
    padding-bottom: 30px;
    text-align: center;
    font-weight: 600;
    font-size: 20px;
    color: #409EFF;
    cursor: pointer;
}

.login-input {
    width: 280px;
    margin-bottom: 20px;
}

.login-submit {
    margin-top: 20px;
    display: flex;
    justify-content: center;
}

.sign-in-container {
    padding: 0 10px;
}

.sign-in-text {
    color: #409EFF;
    font-size: 16px;
    text-decoration: none;
    line-height: 28px;
}

.other-submit {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
    margin-left: 200px;
}
</style>
import{_ as N,r as t,o as c,g as r,w as o,a as e,c as b,f as n,i as B,n as V,b as d,t as A,p as E,h as F}from"./index.5c1af3c9.js";const j={data(){return{isCollapse:!1,nickname:""}},created(){this.nickname=localStorage.getItem("nickname"),this.isAdmin=localStorage.getItem("isAdmin")},methods:{quitLogin(){localStorage.clear(),this.$router.push("/login"),this.$message.success("\u9000\u51FA\u6210\u529F")}}},q=l=>(E("data-v-955a950f"),l=l(),F(),l),H=q(()=>d("div",{class:"logo"},"\u56FE\u4E66\u7BA1\u7406\u7CFB\u7EDF",-1)),L={key:0},U={style:{padding:"0 12px",display:"flex","align-items":"center","justify-content":"center"}},X={style:{"margin-left":"10px",color:"#909399"}};function D(l,u,R,T,s,f){const g=t("House"),a=t("el-icon"),i=t("el-menu-item"),_=t("User"),h=t("el-menu"),x=t("el-aside"),y=t("Expand"),v=t("Fold"),k=t("el-avatar"),p=t("el-dropdown-item"),w=t("el-dropdown-menu"),C=t("el-dropdown"),S=t("el-header"),z=t("router-view"),I=t("el-main"),m=t("el-container");return c(),r(m,null,{default:o(()=>[e(x,{style:V({width:s.isCollapse?"fit-content":"200px"})},{default:o(()=>[H,e(h,{router:"",collapse:s.isCollapse,"default-active":l.$route.path,"active-text-color":"#fff","background-color":"#011528","text-color":"hsla(0,0%,100%,.65)","collapse-transition":!0},{default:o(()=>[l.isAdmin==1?(c(),b("div",L,[e(i,{index:"/media/list"},{default:o(()=>[e(a,null,{default:o(()=>[e(g)]),_:1}),n("\u7CFB\u7EDF\u9996\u9875")]),_:1}),e(i,{index:"/cs/csgl"},{default:o(()=>[e(a,null,{default:o(()=>[e(_)]),_:1}),n("\u51FA\u7248\u793E\u7BA1\u7406")]),_:1}),e(i,{index:"/sp/spgl"},{default:o(()=>[e(a,null,{default:o(()=>[e(_)]),_:1}),n("\u56FE\u4E66\u7BA1\u7406")]),_:1}),e(i,{index:"/dd/ddgl"},{default:o(()=>[e(a,null,{default:o(()=>[e(_)]),_:1}),n("\u4F5C\u8005\u7BA1\u7406")]),_:1})])):B("",!0)]),_:1},8,["collapse","default-active"])]),_:1},8,["style"]),e(m,null,{default:o(()=>[e(S,null,{default:o(()=>[d("div",{style:{cursor:"pointer",height:"100%",padding:"0 12px",display:"flex","align-items":"center"},onClick:u[0]||(u[0]=Z=>s.isCollapse=!s.isCollapse)},[s.isCollapse?(c(),r(a,{key:0,color:"#909399",size:24},{default:o(()=>[e(y)]),_:1})):(c(),r(a,{key:1,color:"#909399",size:24},{default:o(()=>[e(v)]),_:1}))]),e(C,{style:{cursor:"pointer",height:"100%",display:"flex","line-height":"60px"}},{dropdown:o(()=>[e(w,null,{default:o(()=>[e(p,{disabled:""},{default:o(()=>[n("\u4E2A\u4EBA\u4E2D\u5FC3")]),_:1}),e(p,{disabled:""},{default:o(()=>[n("\u4E2A\u4EBA\u8BBE\u7F6E")]),_:1}),e(p,{divided:"",onClick:f.quitLogin},{default:o(()=>[n("\u9000\u51FA\u767B\u5F55")]),_:1},8,["onClick"])]),_:1})]),default:o(()=>[d("div",U,[e(k,{size:26,src:"https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png"}),d("span",X,A(s.nickname),1)])]),_:1})]),_:1}),e(I,null,{default:o(()=>[e(z)]),_:1})]),_:1})]),_:1})}const G=N(j,[["render",D],["__scopeId","data-v-955a950f"]]);export{G as default};
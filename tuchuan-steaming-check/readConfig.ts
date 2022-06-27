import * as fs from 'fs';
if (fs.existsSync('./automated-testing-config.json')) //判断是否存在此文件
{
    //读取文件内容，并转化为Json对象
     let userBugsJson = JSON.parse(fs.readFileSync("./automated-testing-config.json", "utf8"));
     //获取Json里key为data的数据
     const data = userBugsJson['srcurl'];
     for(let i=0;i<data.length;i++){
        console.log(data[i]);
     }
     
}

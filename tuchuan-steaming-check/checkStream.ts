import axios from "axios";
import { spawn } from "child_process";
import inquire from "inquirer";
import * as fs from 'fs';

function gstCmd(x: string) {
    const cmd: string = "";
    const num = x;
    if (num.substring(0, 4) == "rtmp") {
        const cmd = "rtmpsrc";
        return cmd;
    } else if (num.substring(0, 4) == "rtsp") {
        const cmd = "rtspsrc";
        return cmd;
    } else {
        console.log(`wrong ${num}`);
    }
}

function splicing(n: string) {
    const a: string = n;
    const cmd = gstCmd(a);
    const str = [`${cmd}`, `location=${a}`, "!", "fakesink", "dump=true"];
    return str;
}

function spaw(n: string) {
    const a: string = n;
    const str = splicing(a);
    const gst = spawn("gst-launch-1.0", str);
    //console.info(gst);
    console.log(`正在尝试从${a} 拉流`);
    var flag: number = 0;
    gst.stdout.on("data", (data: string) => {
        //console.log("stdout: " + "Successful");
        flag += 1;
        //console.log(flag);
        if (flag == 50) {
            console.log(`${a}拉流成功`);
        }
    });
    gst.stderr.on("data", (data: string) => {
        //console.error(`stderr: ${data}`);
        if (data) {
            console.error(`${a}拉流失败`);
            console.log("Enter \"ctrl+c\" to quit");
        }
    });

    gst.on("close", (code: string) => {
        //console.log(`child process exited with code ${code}`);
        //input();
    });
}

function input() {
    var q = [{ name: "url", message: "请输入url拉流:" }];
    inquire.prompt(q).then((an: { [x: string]: string }) => {
        spaw(an["url"]);
    });
}

function getId() {
    const url: string = "";
    if (fs.existsSync('./automated-testing-config.json')) 
    {
        let userBugsJson = JSON.parse(fs.readFileSync("./automated-testing-config.json", "utf8"));
        const data = userBugsJson['srcurl'];
        for (let i = 0; i < data.length; i++) {
            spaw(data[i]);
        }

    }
    else{
        input();
    }
    return 0;
}

getId();

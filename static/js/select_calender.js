var showIds=[];
var selectedId =null;
var selectedMonth = null;
var selectedYear = null;
var nowMonth = null
var today = new Date();

// 初期表示
window.onload = function () {
    init(today);
};

function init(param){
    for(var i=0;i<12;i++){

        var now = new Date(param);
        if(param ==""){
            now=new Date();
        }
        if(i==0){
            nowMonth=now.getMonth();
        }
        now.setMonth(now.getMonth()+i);
        initCalendar(now,i+1)
    }
}



/**日历初始化，默认当前月份日历
*/
function initCalendar(date_now,i){
    $("#calendarId"+i).empty();
    initCalendarNew("calendarId"+i, date_now.getFullYear(),date_now.getMonth(),date_now);
}


/**
* calendarId: 日历容器id
* year：4位年
* month: 0~11
*/
function initCalendarNew(calendarId,year,month,date_now){
    selectedMonth=month;
    selectedYear=year;
    var cDate = new Date(Date.parse(year+"/"+(month+1)+"/1"));
    var calendar = document.getElementById('calendarId1');
    if(calendarId){
        calendar = document.getElementById(calendarId);
    }
    if(calendar!=null){
        calendar.innerHTML="";
        var cTable = document.createElement("table");
        cTable.classList.add( "caltbl" );
        calendar.appendChild(cTable);
        initCalendarHead(cTable,date_now);
        //计算month的总天数
        var monthDays = getMonthDays(month+1);
        //计算月份开始位置
        var monthBegin = calcStart(cDate);
        //计算月份结束位置
        var monthEnd = monthDays+monthBegin;
        //最后一行最后一个单元格位置
        var end = monthEnd%7==0?monthEnd:monthEnd+(7-monthEnd%7)
        var tr = null;
        var td = null;
        var week = -1;
        for(var i=0;i<end;i++){
            if(i%7==0){
                tr = cTable.insertRow(-1);
                tr.style.height=38;
            }

            td= tr.insertCell(-1);
            week = (i+1)%7;
            //创建单元格
            initCell(td,i-monthBegin,i,i-monthEnd,i>=monthEnd+1,month,week,date_now);
        }
    }
}


/**
* date 单元格位置与该月份第一天单元格位置的差值
* nextMonthDay 单元格位置该月份最后一天单元格位置的差值
* nextFlag 是否为下个月日期
*/
function initCell(cell,date,days,nextMonthDay,nextFlag,month,week,date_now){
    //将差值调整为日期。例如：0调整为1号，-1调整为上个月最后一天
    // date = date+1;
    var currentDateFlag = date_now.getDate()==date && month==nowMonth;
    var showDaysClass = currentDateFlag?"show_now":"hide";
    var previousFlag = false;
    if(date<1){
        date = getMonthDays(date_now.getMonth())+date;
        previousFlag = true;
    }
    if(nextFlag){
        previousFlag = false;
        date = nextMonthDay;
    }


    var showCurClass = currentDateFlag?"current_date":(week==1?"rest_date1":(week==0?"rest_date2":"normal_date"));
    cell.className=currentDateFlag?"selected":"";
    if(previousFlag){
        showCurClass+="_pre";
        showDaysClass+="_pre";
    }else if(nextFlag){
        showCurClass+="_next";
        showDaysClass+="_next";
    }
    //初始化时，如果是今天则设置为选中
    selectedId = currentDateFlag?days:selectedId;
    cell.align="center";
    var daysHtml = "";//days>0?"第"+(days-2)+"天":"";
    var html = "<div id='"+days+"' οnclick='showDayInfo(this)' οnmοuseenter='showDays(this,"+(currentDateFlag)+")'><label class='"+showCurClass+"'>"+date+"</label><br><label id='label_"+days+"' class='"+showDaysClass+"'>"+daysHtml+"</label></div>";
    cell.innerHTML=html;
}


/*カレンダーのhead
*/
function initCalendarHead(table,date_now){
    var tr = table.insertRow(-1);
    td = tr.insertCell(-1);
    td.innerHTML="<label>"+selectedYear+"年"+(selectedMonth+1)+"月</label>";
    td.colSpan=7;
    td.align="center";



    tr = table.insertRow(-1);
    tr.height="30px";
    // var data = ["日","一","二","三","四","五","六"];
    var data = ["日","月","火","水","木","金","土"];
    for(var i=0;i<data.length;i++){
        td = tr.insertCell(-1);
        td.width="50px";
        td.align="center"
        td.innerHTML="<label style='font-size:12px'>"+data[i]+"</label>";
    }
}


function getMonthDays(month){
    var monthDays = 31;
    if(month ==4 || month==6 || month==9 || month==11) {
        monthDays = 30;
    }else if(month==2){
        monthDays=28;
        if((selectedYear%4==0&& selectedYear%100!=0) || selectedYear%400==0){
            monthDays = 29;
        }
    }
    return monthDays;
}


function calcStart(date){
    var week = date.getDay();

    week--;
    // if(week<0){
    //     week+=7;
    // }
    return week;
}


/**
* 兼容IE
*/
function parseDate(val){
    val = val.replace(/-/g,"/");
    return Date.parse(val);
}


/**
* 鼠标滑过展示提示
*/
function showDays(div,currentFlag){
    if(!currentFlag){
        showIds.push(div.id);
        var obj = null;
        for(var i=0;i<showIds.length;i++){
            obj = document.getElementById('label_'+showIds[i]);
            if(obj){
                obj.className="hide";
           }
        }

        //document.getElementById('label_37').style.display="";
        obj = document.getElementById('label_'+div.id);
        if(obj){
            obj.className="show";


            setTimeout(function(){obj.className="hide";showIds.remove(div.id);},1000);
        }


    }

}


function message(msg){
    var msgElement = document.getElementById("msg");
    msgElement.innerHTML+=msg+"<br>";
}


function showDayInfo(parentDiv){
    clearSelected();
    document.getElementById(parentDiv.id).parentNode.className="selected";
    selectedId=parentDiv.id;


}


function clearSelected(){
    if(selectedId){
        if(document.getElementById(selectedId)){
            document.getElementById(selectedId).parentNode.className="";
        }
    }
}




Array.prototype.remove = function(obj){
    var length = this.length;
    var result = -1;
    for(var i=0;i<length; i++){
        if(obj==this[i]){
            result = i;
            this.splice(i,1);
            break;
        }
    }
    return result;
}
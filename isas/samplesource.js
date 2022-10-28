var moduleVersion = '20.10.21.1';
var WeatherName = "샘플소스";
console.log(WeatherName + " 스크립트 호출됨.");
console.log('Version: ' + moduleVersion);

function iSASObject(){
    console.log("iSASObject 생성자 호출");
    this.iSASOut = {};
}

iSASObject.prototype.log = function(logMsg){
    try{
        SASLOG("iSASOBject.Log(" + logMsg + "\")");
    } catch(e){
        console.log("iSASObject.LOG(" + logMsg + "\")");
    }
};

iSASObject.prototype.setError = function(errcode){
    this.iSASInOut.Output = {};
    this.iSASInOut.Output.ErrorCode = errcode.toString(16).toUpperCase();
    this.iSASInOut.Output.ErrorMessage = getCooconErrMsg(errcode.toString(16).toUpperCase());
};

function search(region){
    var CityCode;

    switch(region){

        case "춘천":
            CityCode= '01110675';
            break;

        case "강릉":
            CityCode= '01150615';
            break;
            
        case "백령":
            CityCode= '11720330';
            break;
            
        case "청주":
            CityCode= '16111120';
            break;

        case "서울":
            CityCode= '09140104';
            break;  
            
        case "수원":
            CityCode= '02113128';
            break;
            
        case "대전":
            CityCode= '07110101';
            break;
                        
        case "전주":
            CityCode= '13113135';
            break;
                        
        case "광주":
            CityCode= '05110101';
            break;
                        
        case "목포":
            CityCode= '12110152';
            break;
                        
        case "제주":
            CityCode= '14130116';
            break;
                        
        case "부산":
            CityCode= '08110580';
            break;
            
        default:
            CityCode='09140104';
            break;
    }
    return CityCode;
}


//////


// // 오류처리 함수
//         // this.setError(ErrorCode);
//         // this.iSASInOut.Output.ErrorMessage = ""; (커스텀마이징)
//         // return ErrorCode;
        
//         // 통신 (요청) // Request
//         if (httpRequest.getWithUserAgent(this.userAgent, `https://weather.naver.com/today/${지역명}`)){
//             // 오류처리
//             this.setError(E_IBX_FAILTOGETPAGE);
//             //this.iSASInOut.Output.ErrorMessage = "통신 실패";
//             return E_IBX_FAILTOGETPAGE;
//         }
//         this.log("Main1: ["+ httpRequest.result +"]");

// var currentWeather  = rainy(wetrTxt);

var umbrella;

//비 오면 우산 챙겨
function rainy(currentWeather){
    if (currentWeather == '비'){
        umbrella =  "\n\t *비 온대요. 우산 챙겨요\n\n"
        return umbrella;
    }
    else{
        umbrella =  "\n\t 우산은 필요 없을거 같스빈다!\n\n"
        return umbrella;
    }
}

var clothesArr = [
    ["민소매", "반팔", "짧은 치마", "린넨"], 
    ["반팔", "얇은 셔츠", "반바지", "면바지"], 
    ["블라우스", "긴팔 티", "면바지", "슬랙스"], 
    ["얇은 가디건", "니트", "맨투맨", "후드", "긴바지"], 
    ["자켓", "가디건", "청자켓", "니트", "스타킹", "청바지"]
    ["트랜치 코트", "야상", "점퍼", "스타킹", "기모바지"],
    ["울 코트", "히트텍", "가죽 옷", "기모"],
    ["패딩", "두꺼운 코트", "누빔 옷", "기모", "목도리"]
]; 

function clothesRecommand(clothesArr,avr_temp){
    
    // var _clothesArr = JSON.parse(JSON.stringify(clothesArr));
    // console.log("clothesArr: ["+ JSON.stringify(clothesArr) +"]");

    var cloth= [];    
    if (avr_temp >= 28){
        cloth.push(clothesArr[0]);
        return cloth;
    }
    else if (avr_temp >= 27){
        cloth.push(clothesArr[1]);
        return cloth;
    }
    else if (avr_temp >= 20){
        cloth.push(clothesArr[2]);
        return cloth;
    }
    else if (avr_temp >= 17){
        cloth.push(clothesArr[3]);
        return cloth;
    }
    else if  (avr_temp >= 12){
        cloth = _clothesArr[4];

        return cloth[4];
    }
    else if (avr_temp >= 6){
        cloth.push(clothesArr[5]);
        return cloth;
    }
    else if (avr_temp >= 4){
        cloth.push(clothesArr[6]);
        return cloth;
    }
    else if (avr_temp <= 3){
        cloth.push(clothesArr[7]);
        return cloth;
    }

    // var cloth =[];
    // if (avr_temp >= 28){
    //     cloth = clothesArr[0]
    // }
    // else if (avr_temp >= 27){
    //     cloth = clothesArr[1]
    // }
    // else if (avr_temp >= 20){
    //     cloth = clothesArr[2]
    // }
    // else if (avr_temp >= 17){
    //     cloth = clothesArr[3]
    // }
    // else if  (avr_temp >= 12){
    //     cloth = clothesArr[4]
    // }
    // else if (avr_temp >= 9){
    //     cloth = clothesArr[5]
    // }
    // else if (avr_temp >= 5){
    //     cloth = clothesArr[6]
    // }
    // else if (avr_temp <= 4){
    //     cloth = clothesArr[7]
    // }
    // console.log("TEST["+ avr_temp +"]:["+ cloth +"]");
    // console.log("TEST["+ avr_temp +"]:["+ JSON.stringify(cloth) +"]");

    //return cloth

}



var 날씨 = function(){
    console.log(WeatherName + " 샘플구조체 생성자 호출");
    this.errorMsg = "";
    this.host = "";
    this.userAgent = '{';
    this.userAgent += '"Accept":"image/webp,image/apngimage/*,*/*;q=0.8"';
    this.userAgent += '"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"';
    this.userAgent += '}';
};  

날씨.prototype = Object.create(iSASObject.prototype);

날씨.prototype.날씨정보조회 =function(aInput){
    this.log(WeatherName + " 날씨정보조회 호출[" + aInput + "]");
    try{
        system.setStatus(IBXSTATE_CHECKPARAM, 10);

        var input = dec(aInput.Input);

        var regionName = search(input.regionName);
        this.log("input:" + regionName);

        // 스크래핑 개발 기본

        // 1. 통신 (요청) // Request
        //httpRequest.get(url); Header 새팅 불필요 시
        //httpRequest.getWithUserAgent(userAgent, url); Header 새팅 필요 시
        var userAgent = '{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}';
        // httpRequest.getWithUserAgent(userAgent, 'https://www.naver.com/my.html');


        httpRequest.getWithUserAgent(userAgent, `https://weather.naver.com/today/${regionName}`);

        // httpRequest.getWithUserAgent(userAgent, 'https://weather.naver.com/today/03310109');

        var ResultStr = httpRequest.result;


        httpRequest.getWithUserAgent(userAgent, `https://weather.naver.com/air/${regionName}`);


        // httpRequest.getWithUserAgent(userAgent, 'https://weather.naver.com/air/03310109');

        var ResultAirStr = httpRequest.result;


        // 2. 결과 (응답) // Response
        // this.log ==> console.log
        this.log("Main1: ["+ ResultStr +"]");

        // 3. 결과처리 (결과포맷)
        //var ResTem = StrGrab(ResultStr, '<div class="email MY_EMAIL">', '</div>');
        
        // "regionName":"춘천"

        //aIndex = 1부터 시작
        // var clothesArr = [
        //     ["민소매", "반팔", "짧은 치마", "린넨"], 
        //     ["반팔", "얇은 셔츠", "반바지", "면바지"], 
        //     ["블라우스", "긴팔 티", "면바지", "슬랙스"], 
        //     ["얇은 가디건", "니트", "맨투맨", "후드", "긴바지"], 
        //     ["자켓", "가디건", "청자켓", "니트", "스타킹", "청바지"]
        //     ["트랜치 코트", "야상", "점퍼", "스타킹", "기모바지"],
        //     ["울 코트", "히트텍", "가죽 옷", "기모"],
        //     ["패딩", "두꺼운 코트", "누빔 옷", "기모", "목도리"]
        // ]; 


        var 날씨정보조회 = [];
        
       

            var regionName = StrGrab(ResultStr, '"fullAreaName":"', '"');
            var mareaNm = StrGrab(ResultStr, '"mareaNm":"', '"');
            var today = StrGrab(ResultStr, '<strong class="day">오늘</strong><span class="date">', '</span>');
           
            var ul_str  = StrGrab(ResultStr, 'class="box_color">', '</ul>');
            var li_tmr = StrGrab(ul_str, '<li', '</li>', 2);
           var tommorow_morning = StrGrab(li_tmr,'<span class="weather_text">', '</span>',1);
           
           var tommorow_evening = StrGrab(li_tmr,'<span class="weather_text">', '</span>',2)
            // var 오전 =  StrGrab();

            var wetrTxt = StrGrab(ResultStr, '<span class="weather">', '</span>');   
            
            var currentWeather  = rainy(wetrTxt);



            var aplTm = StrGrab(ResultStr, '<span class="blind">현재 온도</span>', '<span class="degree">');
            // console.log("circuit" +circuit );


            // var aplTm = StrGrab(ResultStr, '"stationO3Legend1":"', '"');


            // var rainfall = StrGrab(ResultStr, '<dl><dt class="blind">강수확률</dt><dd>', '</dd>');

            var rainfall_mor = StrGrab(ResultStr, '<span class="blind">강수확률</span>', '</span>',  1);
            
            var rainfall_eve = StrGrab(ResultStr, '<span class="blind">강수확률</span>', '</span>',  2);
            var lowest = StrGrab(ResultStr, '<span class="lowest"><span class="blind">최저기온</span>', '</span>');
            var highest =  StrGrab(ResultStr, '<span class="highest"><span class="blind">최고기온</span>', '</span>');
            console.log("lowest:::" + lowest);
            console.log("highest:::" + highest);

            var avr_temp = ((parseFloat(highest) + parseFloat(lowest))/2);
            console.log("avr_temp:::" + avr_temp);

             var todayclothes = clothesRecommand(clothesArr, avr_temp);
            console.log("todayclothes:::" + JSON.stringify(todayclothes));

            var cnPm10Value =  StrGrab(ResultAirStr, '<span class="value _cnPm10Value">', '</span>');
            var cnPm10Grade =  StrGrab(ResultAirStr, '<span class="grade _cnPm10Grade">', '</span>');
            var cnPm25Value = StrGrab(ResultAirStr, '<span class="value _cnPm25Value">', '</span>');

            var cnPm25Grade = StrGrab(ResultAirStr, '<span class="grade _cnPm25Grade">', '</span>');

            var item = {};

            
            var tommorow_item = {};

            item.regionName = regionName;
            item.mareaNm = mareaNm;
            item.today = today;
            item.wetrTxt = wetrTxt;

            item.avr_temp = avr_temp + '';
            item.todayclothes = todayclothes;


            item.aplTm = aplTm;
            item.rainfall_mor= rainfall_mor;
            item.rainfall_eve= rainfall_eve;
            item.lowest= lowest+"C";
            item.highest= highest+"C";
            item.cnPm10Value= cnPm10Value;
            item.cnPm10Grade= cnPm10Grade;
            item.cnPm25Value=cnPm25Value;
            item.cnPm25Grade=cnPm25Grade;

            // item.tommorow_mor =tommorow_mor;

            item.currentWeather=currentWeather;
            날씨정보조회.push(item);


            // var tommorow_morning = StrGrab(ResultStr, '<strong class="day">내일</strong><span class="date">', '</span>');

            var tommorow_date = StrGrab(ResultStr, '<strong class="day">내일</strong><span class="date">', '</span>');

            
            // tommorow_item.tommorow_morning = tommorow_morning;
 
                        
            var rainfall_nextmorning = StrGrab(ResultStr, '<span class="blind">강수확률</span>', '</span>',  3);
            var rainfall_nextevening = StrGrab(ResultStr, '<span class="blind">강수확률</span>', '</span>',  4);
            // var tommorow_wetrTxt = StrGrab(ResultStr, '<span class="label tomorrow">내일</span><i class="ico _cnLazy" data-ico="ico_wt2"><span class="blind">', '</span>'); 
           
            tommorow_item.tommorow_date =tommorow_date;
            tommorow_item.rainfall_nextmorning=rainfall_nextmorning;
            tommorow_item.rainfall_nextevening=rainfall_nextevening;

           
            tommorow_item.tommorow_morning = tommorow_morning;
            tommorow_item.tommorow_evening = tommorow_evening;
            // tommorow_item.tommorow_wetrTxt = tommorow_wetrTxt;

            날씨정보조회.push(tommorow_item);
        
        // var 날씨정보조회 = [];
        // var item = {};

        // item.지역명 = '서울';
        // item.온도 = '12.1';
        // item.상태 = '맑음';
        // 날씨정보조회.push(item);
    
        // var item = {};

        // item.지역명 = '부산';
        // item.온도 = '12.2';
        // item.상태 = '맑음';
        // 날씨정보조회.push(item);

        // OUTPUT
        this.iSASInOut.Output ={};
        this.iSASInOut.Output.ErrorCode = "00000000";
        this.iSASInOut.Output.ErrorMessage = "";
        this.iSASInOut.Output.Result = {};
        // this.iSASInOut.Output.Result.이메일 = ResTem;
        this.iSASInOut.Output.Result.날씨정보조회 = 날씨정보조회;
        
        return S_IBX_OK;
    } catch(e){
        this.log("Exception " + e.message);
        this.setError(E_IBX_UNKNOWN);
        return E_IBX_UNKNOWN;
    } finally{
        system.setStatus(IBXSTATE_DONE, 100);
        this.log(WeatherName + " 샘플함수 finally");
    }
};


////



function OnInit() {
    console.log("OnInit()");
    var result = true;
    try {
        //필요한거 로드
        system.include("iSASTypes");
        system.setStatus(IBXSTATE_BEGIN, 0);
        result = false;
    } catch (e) {  
        console.log("Exception OnInit:[" + e.message + "]");        
    } finally {
        //flase 리턴
        return result;
    }
}

function Execute(aInput) {
    console.log("Execute[" + aInput + "]");
    try {
        console.log("Init Default Error");
        iSASObj = JSON.parse(aInput);
        iSASObj.Output = {};
        iSASObj.Output.ErrorCode = '8000F110';
        iSASObj.Output.ErrorMessage = "해당 모듈을 실행하는데 실패 했습니다.";

        OnInit();

        iSASObj = JSON.parse(aInput);
        var ClassName = iSASObj.Class;
        var ModuleName = iSASObj.Module;
        if (Failed(SetClassName(ClassName, ModuleName))) {
            iSASObj.Output = {};
            iSASObj.Output.ErrorCode = '8000F111';
            iSASObj.Output.ErrorMessage = "Class명과 Job명을 확인해주시기 바랍니다.";
        } else {
            obj.iSASInOut = "";
            OnExcute(0, JSON.stringify(iSASObj));

            console.log("결과 테스트 [" + obj.iSASInOut + "]");

            if (obj.iSASInOut != "")
                iSASObj = obj.iSASInOut;
        }
    } catch (e) {
        console.log("exception:[" + e.message + "]");
    } finally {
        return JSON.stringify(iSASObj);
    }
}
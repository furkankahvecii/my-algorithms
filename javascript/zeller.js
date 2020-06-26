function updateDays()
{
    if(document.getElementById("month").value == 2)
    {
        if (parseInt(document.getElementById("year").value) % 4 != 0)
        {
            document.getElementById("day").max = 28;
        }
        else
        {
            if (parseInt(document.getElementById("year").value) % 100 != 0)
            {
                document.getElementById("day").max = 29;
            }
            else
            {
                if (parseInt(document.getElementById("year").value) % 400 != 0)
                {
                    document.getElementById("day").max = 28;
                }
                else
                {
                    document.getElementById("day").max = 29;
                }
            }
        }
    }  
    else if(document.getElementById("month").value == 4 || document.getElementById("month").value == 6 || document.getElementById("month").value == 9 || document.getElementById("month").value == 11)
    {
        document.getElementById("day").max = 30;
    }
    else
    {
        document.getElementById("day").max = 31;
    }
            
}

function clearAnswer()
{
    document.getElementById("answer").innerHTML = "";
}
        
function Zeller()
{
    var D = parseInt(document.getElementById("day").value);
    var M = parseInt(document.getElementById("month").value);
    var Y = parseInt(document.getElementById("year").value);
            
    if (M < 3)
    {
        M = M + 12;
        Y = Y - 1;
    }
            
    var C = Math.floor(Y / 100);
    var K = Y - (100 * C);
            
    var S = Math.floor(2.6 * M - 5.39) + Math.floor(K / 4) + Math.floor(C / 4) + D + K - (2 * C);
            
    ans = S - (7 * Math.floor(S / 7));

    switch(ans)
    {
        case 0 : Day = "Sunday"; break;
        case 1 : Day = "Monday"; break;
        case 2 : Day = "Tuesday"; break;
        case 3 : Day = "Wednesday"; break;
        case 4 : Day = "Thursday"; break;
        case 5 : Day = "Friday"; break;
        case 6 : Day = "Saturday"; break;
    }
    
    document.getElementById("answer").innerHTML = "It was a " + Day;
}

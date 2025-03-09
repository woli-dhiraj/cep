function calculateConsumption() {
    let devices = document.getElementById("devices").value;
    let area = document.getElementById("area").value;
    let actualUsage = document.getElementById("actualUsage").value;
    
    if (devices <= 0 || area <= 0 || actualUsage <= 0) {
        document.getElementById("result").innerHTML = "<p style='color:red;'>Please enter valid numbers.</p>";
        return;
    }

    let expectedConsumption = (devices * 5) + (area * 0.2);

    let resultText = `<p>Expected Consumption: <b>${expectedConsumption.toFixed(2)} kWh</b></p>`;
    resultText += `<p>Actual Consumption: <b>${actualUsage} kWh</b></p>`;

    if (actualUsage > expectedConsumption) {
        resultText += `<p style="color: red;">Your electricity consumption is higher than expected!</p>`;
        resultText += `<h3>Tips to Save Energy:</h3>
            <ul style="text-align: left; display: inline-block;">
                <li>Use LED bulbs instead of incandescent lights.</li>
                <li>Unplug devices when not in use.</li>
                <li>Use energy-efficient appliances.</li>
                <li>Optimize air conditioning and heating usage.</li>
                <li>Switch off lights when not needed.</li>
            </ul>`;
    } else {
        resultText += `<p style="color: green;">Great job! Your energy consumption is within the expected range.</p>`;
    }

    document.getElementById("result").innerHTML = resultText;
}

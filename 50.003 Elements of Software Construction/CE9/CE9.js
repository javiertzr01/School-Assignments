const MongoClient = require("mongodb").MongoClient;
const url = "mongodb://localhost:27017/";
const client = new MongoClient(url);

function generate_Number() {
    // Generates a number between 0 (Inclusive) and 100 (Inclusive)
    return Math.floor(Math.random() * 101);
}

function reset() {
    // Reset the database
    try {
        const dbo = client.db("sutd");
        dbo.dropDatabase();
    } catch (err) {
        console.log(err);
    }
}

async function main() {
    reset();

    // Values for Part 3
    var objArray = Array(20);
    var studentNames = [
        "Liam",
        "Noah",
        "Oliver",
        "Elijah",
        "James",
        "William",
        "Benjamin",
        "Lucas",
        "Henry",
        "Theodore",
        "Olivia",
        "Emma",
        "Charlotte",
        "Amelia",
        "Ava",
        "Sophia",
        "Isabella",
        "Mia",
        "Evelyn",
        "Harper",
    ];
    for (let i = 0; i < 20; i++) {
        document = {
            studentid: `${i + 1}`,
            average_grade: "0",
            full_name: studentNames[i],
            grades: [],
            term: "0",
        };
        objArray[i] = document;
    }

    try {
        // Part 1
        const dbo = client.db("sutd");

        // Part 2
        const collec = dbo.collection("students");

        // Part 3
        await collec.insertMany(objArray);
        // console.log("created");

        // Part 4
        var curs = collec.find();
        while (await curs.hasNext()) {
            document = await curs.next();
            for (let i = 0; i < 8; i++) {
                for (let gradeIdx = 0; gradeIdx < 4; gradeIdx++) {
                    document["grades"].push(generate_Number());
                }
                document["term"] = (Number(document["term"]) + 1).toString();
            }

            // console.log(document['term']);
            // console.log(document['grades']);

            // Part 5
            const arr = document["grades"];
            let sum = 0;
            arr.forEach((num) => {
                sum = sum + num;
            });
            document["average_grade"] = sum / arr.length;
            // console.log(document['grades'])
            // console.log(document["average_grade"]);
            await collec.updateOne(
                { _id: document._id },
                {
                    $set: {
                        average_grade: document.average_grade,
                        grades: document.grades,
                        term: document.term,
                    },
                }
            );
        }

        // Part 6
        const result = await collec.find({}).sort({"average_grade": -1}).toArray();
        result.forEach((document) => {
            console.log(document);
        })
    } finally {
        await client.close();
    }
}

main().catch(console.dir);

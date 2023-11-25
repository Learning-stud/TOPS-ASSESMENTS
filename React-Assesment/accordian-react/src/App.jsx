import { useState } from "react";

const Accordion = () => {
  // Defined state to manage accordion visibility
  const [isOpen, setIsOpen] = useState(Array(4).fill(false)); 

  //  Toggling visibility on click of title
  const toggleAccordion = (index) => {
    //  Toggling visibility of accordion body
    const updatedIsOpen = [...isOpen];
    updatedIsOpen[index] = !updatedIsOpen[index];
    setIsOpen(updatedIsOpen);
  };

  return (
    <div className="flex justify-center items-center h-screen  bg-slate-600 ">
      <div className="  w-full sm:w-3/4 md:w-1/2 lg:w-1/3 xl:w-1/4 mt-8  ">

        {Array(4)
          .fill(null)
          .map((_, index) => (
            <div key={index} className="   mb-4 text-slate-950">
              {/* Accordion Header */}
              <div
               
                onClick={() => toggleAccordion(index)}
                className="cursor-pointer bg-gray-200 p-4 border-b border-gray-300"
              >
                Accordion Title {index + 1}
              </div>

       
              {isOpen[index] && (
                <div className="p-4 border border-gray-300">
                  \Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Natus perferendis, perspiciatis asperiores reprehenderit,
                  aliquam quasi, assumenda neque amet cum quisquam quo
                  inventore? Porro tempore, illum odio dolores quam impedit
                  similique?
                </div>
              )}
            </div>
          ))}
      </div>
    </div>
  );
};

export default Accordion;
